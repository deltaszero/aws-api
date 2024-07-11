import requests
import json
import boto3
from openai import OpenAI
from botocore.exceptions import ClientError

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


def gpt_response(text):
    try:
        client = OpenAI(
            api_key=get_secret()['OPENAI_API_KEY']
        )
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a physicist assistant, skilled in explain complex concepts about many subjects."},
                {"role": "user", "content": text},
            ]
        )
        return str(chat_completion.choices[0].message.content)
    except Exception as e:
        print(f"An Error Occurred: {str(e)} @ gpt_response")
        return "An Error Occurred"


def send_message(text_user, number_user):
    try:
        # token = os.getenv('META_API_TOKEN')
        token = get_secret()['META_API_TOKEN']
        api_url = "https://graph.facebook.com/v19.0/301453326394584/messages"
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": str(number_user),
            "type": "text",
            "text": {
                "body": text_user,
            }
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"An Error Occurred: {str(e)} @ send_message")
        return False