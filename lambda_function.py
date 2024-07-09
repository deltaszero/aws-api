import awsgi
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def lambda_handler(event, context):
    return awsgi.response(app, event, context)
