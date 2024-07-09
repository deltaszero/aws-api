import awsgi
from flask import Flask, jasonify

app = Flask(__name__)

@app.route('/')
def index():
    return jasonify({'message': 'Welcome to the Flask API!', 'status': 200})

@app.route('/version')
def version():
    return jasonify({'version': '1.0.0', 'status': 200})

def lambda_handler(event, context):
    return awsgi.response(app, event, context)
