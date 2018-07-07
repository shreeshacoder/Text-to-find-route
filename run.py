# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json, urllib
from urllib import urlencode
import googlemaps
import re

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    req = request.form['Body']
    directions = find_direction(req)
    # Add a message
    resp.message(directions)

    return str(resp)

def find_direction(message):
	# origin = "Sydney Town Hall"
	# destination = "Parramatta, NSW"
	print message
	origin = message.split(',')[0]
	destination = message.split(',')[1]
	url = 'https://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((('origin', origin),('destination', destination),('key','AIzaSyAda0Qn_rVoqu7I2RtyjSqJqYaLOoiaUhg')))
	ur = urllib.urlopen(url)
	result = json.load(ur)
	line = ""
	res = ""
	for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    		j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
    		j = re.sub('<.*?>', ' ', j)
    		count = str(i + 1)
    		res = res+line+"\n"
    		line = count+") "+j
	return res

if __name__ == "__main__":
    app.run(debug=True)