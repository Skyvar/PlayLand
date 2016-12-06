#!/usr/bin/env python

#import requests

class temperature:
	def temperature(zipcode):
	    url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(zipcode) + "&APPID=7d309f4fac16c6fe0779b433aa566dbf"
	    weather = requests.get(url).json()
	    #degree_symbol=
	    ktemp = weather['main']['temp']
	    ftemp = (ktemp * 9/5) - 459.67
	    print("The current temp for zip " + str(zipcode) + " is:\n")
	    print(str(int(ftemp)) + str(degree_symbol) + "F")
	
