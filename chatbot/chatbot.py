import os
from flask import Flask, request
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client 

# sid = os.getenv("TWILIO_SID")
# auth_token = os.getenv("TWILIO_TOKEN")

# client = Client(sid, auth_token)

app = Flask(__name__)

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route("/")
def home():
    return "Home"

@app.route("/message")
def reply():
    message = request.form.get("Body").lower()
    respond(message)
    return None 

app.run(debug=True, port=5020)