import boto3
import json
from botocore.exceptions import ClientError
from flask import Flask, jsonify, request, render_template


def get_secret():
    secret_name = "whatsapp_api_secrets"
    region_name = "sa-east-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as _error_:
        raise _error_
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Flask API!', 'status': 200})

@app.route('/version')
def version():
    return jsonify({'version': '1.0.0', 'status': 200})
