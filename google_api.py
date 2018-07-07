import json, urllib
from datetime import datetime
from urllib import urlencode
import googlemaps
import re


def find_direction():
	#origin = message.split(' ',0)
	#destination = message.split(' ',1)
	origin = "Sydney Town Hall"
	destination = "Parramatta, NSW"
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
	print res
	#print result
	#url = "https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}4&key=AIzaSyAda0Qn_rVoqu7I2RtyjSqJqYaLOoiaUhg"
	# gmaps = googlemaps.Client(key='AIzaSyAda0Qn_rVoqu7I2RtyjSqJqYaLOoiaUhg')
	# # Geocoding an address
	# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
	# # Look up an address with reverse geocoding
	# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
	# # Request directions via public transit
	# now = datetime.now()
	# directions_result = gmaps.directions("Sydney Town Hall","Parramatta, NSW",mode="transit",departure_time=now)
	# print directions_result
	# origin = ""
	# responde = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}4&key=AIzaSyAda0Qn_rVoqu7I2RtyjSqJqYaLOoiaUhg")
	# info = responde["routes"]
	# data = info[0]
	# legs = data["legs"]
	# address = legs[0]
	# location = address["end_address"]
	# return location
find_direction()
