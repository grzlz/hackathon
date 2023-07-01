import os
from flask import Flask
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client 

# sid = os.getenv("TWILIO_SID")
# auth_token = os.getenv("TWILIO_TOKEN")

# client = Client(sid, auth_token)

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/message")
def reply():
    return None 

app.run(debug=True, port=5020)