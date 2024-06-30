from flask import Flask, request
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Disable Flask's default logging
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/url', methods=['POST'])
def receive_url():
    data = request.get_json()
    url = data.get('url')
    print(url)  # Print the URL only
    return '', 200  # Return an empty response with status 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
