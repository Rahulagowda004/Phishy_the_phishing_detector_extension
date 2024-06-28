import warnings
warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', message="A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0")

from flask import Flask, request,render_template,jsonify
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import urllib.parse

app = Flask(__name__)

@app.route('/receive_url', methods=['POST'])
def receive_url():
    data = request.json
    url = data.get('url')
    
    # You can now use the URL in your Python code
    print(f'Received URL: {url}')
    
    # Return a response
    return jsonify({"status": "success", "url": url}), 200

@app.route('/send_data', methods=['GET'])
def receive_data():
    user_input = request.args.get('data')
    if user_input:
        # Decode the URL-encoded input
        decoded_input = urllib.parse.unquote(user_input)
        
        # Remove specific unwanted characters
        decoded_input = decoded_input.replace('GET /send_data?data=', '').replace(' %20 HTTP/1.1', '')
        
        print(f'Received input from HTML: {decoded_input}')
        
        model_directory = r"model"
        tokenizer = AutoTokenizer.from_pretrained(model_directory)
        model = AutoModelForSequenceClassification.from_pretrained(model_directory)
        
        inputs = tokenizer(decoded_input, return_tensors="pt")

        # Ensure the input tensors are on the correct device (GPU if available)
        inputs = {key: tensor.to(model.device) for key, tensor in inputs.items()}

        # Perform inference
        with torch.no_grad():
            outputs = model(**inputs)

        # Get predicted probabilities
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

        # Get predicted label (assuming a binary classification)
        predicted_label = probs.argmax().item()
        
        if predicted_label == 1:
            result1 = 'site is not secure'
        elif predicted_label == 0:
            result1 = 'site is secure'
            
        print(f"Predicted Label: {result1}")
        return render_template('plugin_ui.html', result=result1)
        
    return result1

if __name__ == '__main__':
    app.run(port=8000)