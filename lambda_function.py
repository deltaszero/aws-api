from flask import Flask
import awsgi

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def handler(event, context):
    return awsgi.response(app, event, context)
