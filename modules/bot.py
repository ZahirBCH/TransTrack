from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get sensitive information from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)

def send_whatsapp_message(to, message):
    message = client.messages.create(
        body=message,
        from_=whatsapp_number,
        to=f'whatsapp:{to}'
    )
    return message.sid