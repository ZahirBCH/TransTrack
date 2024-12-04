from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from modules.trip_management import create_trip

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to TransTrack API!"

# Exemple de route pour créer un voyage
@app.route('/create_trip', methods=['POST'])
def create_trip_route():
    data = request.get_json()
    response = create_trip(data)
    return jsonify(response)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'next trip' in incoming_msg:
        msg.body("The next trip is scheduled for December 15th.")
    else:
        msg.body("Sorry, I didn't understand that. Please ask about the next trip.")

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)