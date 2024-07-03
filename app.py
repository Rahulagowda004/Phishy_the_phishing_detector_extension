import warnings
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
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

@app.route('/url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data.get('url')
    print(url)  # Print the URL only
    result_url = classifier.classify_url(url)
    print("SITE :", result_url)
    return jsonify(result_url=result_url), 200  # Return the result_url in the response

@app.route('/user_input', methods=['POST'])
def receive_user_input():
    data = request.get_json()
    user_input = data.get('user_input')
    print(user_input)  # Print the user_input only
    result_input = classifier.classify_url(user_input)
    print("Input :", result_input)
    return jsonify(result_input=result_input), 200  # Return the result_input in the response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
