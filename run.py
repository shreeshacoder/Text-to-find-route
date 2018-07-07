# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    #req = request.form['Body']
    #status = find_direction(req)
    # Add a message
    resp.message("Thank you for the message")

    return str(resp)

def find_direction(message):
	origin = message.split(' ',0)
	destination = message.split(' ',1)
	responde = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}4&key=AIzaSyAda0Qn_rVoqu7I2RtyjSqJqYaLOoiaUhg")
	info = responde["routes"]
	data = info[0]
	legs = data["legs"]
	address = legs[0]
	location = address["end_address"]
	return location

if __name__ == "__main__":
    app.run(debug=True)