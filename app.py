import warnings
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask, request
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

classficier = URLClassifier()

@app.route('/url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data.get('url')
    # print(url)  # Print the URL only
    return '', 200  # Return an empty response with status 200

@app.route('/user_input', methods=['POST'])
def receive_user_input():
    data = request.get_json()
    user_input = data.get('user_input')
    # print(user_input)  # Print the user_input only
    return '', 200  # Return an empty response with status 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
