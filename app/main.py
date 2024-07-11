from flask import Flask, jsonify, request
import app.util.utils as utils
import app.util.serving as serving
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Flask API!', 'status': 200})

@app.route('/version')
def version():
    return jsonify({'version': '1.0.0', 'status': 200})

@app.route('/whatsapp', methods=['GET'])
def verify():
    """
    According to documentation, it needs to get hub.verify_token and hub.challenge
    """
    try:
        access_token = "CRISTIANORONALDO"
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if (token is not None) and (token == access_token) and (challenge is not None):
            return challenge
        else:
            return "Invalid Request or Verification Token", 400
    except Exception as e:
        return "An Error Occurred: " + str(e), 400

@app.route('/whatsapp', methods=['POST'])
def receive_message():
    try:
        data = request.get_json()
        entry = (data['entry'])[0]
        changes = (entry['changes'])[0]
        value = changes['value']
        message = (value['messages'])[0]
        number = message['from']
        
        text = utils.get_text_user(message)
        reply_message(serving.gpt_response(text), number)

        return "EVENT_RECEIVED"
    except Exception as e:
        print(f"An Error Occurred: {str(e)} @ receive_message")
        print("Data: ", data)
        return "EVENT_RECEIVED"

def reply_message(text, number):
    try:
        serving.send_message(text, number)
        return "Message sent successfully"
    except Exception as e:
        return "An Error Occurred: " + str(e)