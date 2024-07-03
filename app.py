import warnings
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from urllib.parse import urlparse, parse_qs, urlunparse
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
from pipeline import URLClassifier

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

@app.route('/url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data.get('url')
    url = clean_url(url)
    print(url)
    label_url = classifier.classify_url(url)
    if label_url == 0 : 
        result_url = "site is secure"
    elif label_url == 1 :
        result_url = "site is not secure"
    print("SITE :", result_url)
    return jsonify(result_url=result_url), 200  # Return the result_url in the response

@app.route('/user_input', methods=['POST'])
def receive_user_input():
    data = request.get_json()
    user_input = data.get('user_input')
    print(user_input)  # Print the user_input only
    label_input = classifier.classify_url(user_input)
    if label_input == 0 :
        result_input = "input is secure"
    elif label_input == 1 :
        result_input = "input is not secure"
    print("Input :", result_input)
    return jsonify(result_input=result_input), 200  # Return the result_input in the response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)