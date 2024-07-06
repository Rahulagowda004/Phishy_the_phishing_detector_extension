import warnings
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from urllib.parse import urlparse, parse_qs, urlunparse
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
from pipeline import URLClassifier
import json
import os

warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', message="A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0")

app = Flask(__name__)
CORS(app)

# Disable Flask's default logging
log = logging.getLogger('werkzeug')
log.disabled = True

classifier = URLClassifier()

def clean_url(input_url):
    # Parse the URL
    parsed_url = urlparse(input_url)
    # Extract scheme, netloc (domain), and path
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    path = parsed_url.path
    # Extract and clean query parameters
    if parsed_url.query:
        query_params = parse_qs(parsed_url.query)
        if 'q' in query_params:
            query = f"q={query_params['q'][0]}"
        else:
            query = ""
    else:
        query = ""
    # Reconstruct the cleaned URL
    cleaned_url = urlunparse((scheme, netloc, path, '', query, ''))
    return cleaned_url

def append_to_json(text, label):
    file_path = "artifacts/data.json"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append({"text": text, "label": label})

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/url', methods=['POST'])
def receive_url():
    phishy_count = 0
    non_phishy_count = 0
    data = request.get_json()
    url = data.get('url')
    cleaned_url = clean_url(url)
    print(cleaned_url)
    label_url = classifier.classify_url(cleaned_url)
    append_to_json(url, label_url)
    result_url = "site is secure" if label_url == 0 else "site is not secure"
    if result_url == "site is secure" :
        phishy_count = phishy_count + 1
    elif result_url == "site is not secure" :
        non_phishy_count = non_phishy_count + 1
    print("SITE:", result_url)
    return jsonify(result_url=result_url,url = cleaned_url,phishy_count = phishy_count,non_phishy_count = non_phishy_count), 200

@app.route('/user_input', methods=['POST'])
def receive_user_input():
    data = request.get_json()
    user_input = data.get('user_input')
    print(user_input)
    label_input = classifier.classify_url(user_input)
    result_input = "input is secure" if label_input == 0 else "input is not secure"
    append_to_json(user_input, label_input)
    print("Input:", result_input)
    return jsonify(result_input=result_input), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
