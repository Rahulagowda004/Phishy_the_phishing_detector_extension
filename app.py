import warnings
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask, request,render_template
from flask_cors import CORS
import logging
from pipeline import URLClassifier

warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', message="A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0")

app = Flask(__name__,template_folder='extension/templates')
CORS(app)

# Disable Flask's default logging
log = logging.getLogger('werkzeug')
log.disabled = True

classficier = URLClassifier()

@app.route('/url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data.get('url')
    print(url)  # Print the URL only
    result = classficier.classify_url(url)
    print(result)
    if result == 0:
        print("the url is secure")
        return render_template("index.html", url_result = "the url is secure")
    else :
        print("the url is not secure")
        return render_template("index.html", url_result = "the url is not secure")
    return '', 200  # Return an empty response with status 200

@app.route('/user_input', methods=['POST'])
def receive_user_input():
    data = request.get_json()
    user_input = data.get('user_input')
    print(user_input)  # Print the user_input only
    result = classficier.classify_url(user_input)
    print(result)
    if result == 0 :
        print("the content is secure")
        return render_template("index.html",user_input_result = "the content is secure")
    else : 
        print("")
        return render_template("index.html",user_input_result = "the content is not secure")
    return '', 200  # Return an empty response with status 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
