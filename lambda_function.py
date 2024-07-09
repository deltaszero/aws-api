import awsgi
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Flask API!', 'status': 200})

@app.route('/version')
def version():
    return jsonify({'version': '1.0.0', 'status': 200})

def lambda_handler(event, context):
    return awsgi.response(app, event, context)
