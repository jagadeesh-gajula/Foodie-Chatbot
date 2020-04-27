from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import cities
import smtplib 
import pprint, json
import zomatopy
import requests





cities = ['ahmedabad','banglore','bengaluru',' bangalore', 'chennai','madras', 'delhi','new delhi', 'hyderabad',
		 'kolkata', 'culcatta' ,'mumbai','bombay', 'pune', 'agra', 'ajmer','aligarh', 'amravati','amaravati', 'amritsar',
		  'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 
		  'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro', 'chandigarh', 'coimbatore', 
		  'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad', 
		  'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 
		  'guwahati', 'hamirpur', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 
		  'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur', 
		  'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana', 
		  'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 
		  'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna', 
		  'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 
		  'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat', 
		  'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur',
		   'vadodara', 'varanasi', 'vasai-virar', 'vijayawada','vijaywada', 'visakhapatnam', 'vellore', 
		   'warangal']


res=''

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'


	def fetch(self,loc='delhi',cuisine='north indian',price='high'):
		
		#adjust the price range
		price_min = 0
		price_max = 99999
		if price == 'low':
			price_max = 300
		elif price == 'mid':
			price_min = 300
			price_max = 700
		elif price == 'high':
			price_min = 700
		else:
			price_min = 300
			price_max = 9999
		
		# provide API key and initialise a 'zomato app' object
		config={ "user_key": "4734a24a9caf5cd3ae0a0e9161e66212"}
		zomato = zomatopy.initialize_app(config)
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'north':50,'south':85,'indian':80}

		# get_location gets the lat-long coordinates of 'loc'
		loc_detail=zomato.get_location(loc, 1)
		loc_detail=json.loads(loc_detail)
		if loc_detail['status'] == 'success':
			lat = loc_detail['location_suggestions'][0]['latitude']
			lon = loc_detail['location_suggestions'][0]['longitude']
			data =  zomato.restaurant_search( query='', latitude=lat, longitude=lon, cuisines=str(cuisines_dict.get(cuisine)), limit=100)
			data = json.loads(data)
			global res
			if data['results_found'] > 0:
				added=0
				for i in data['restaurants']:
					if i['restaurant']['average_cost_for_two'] > price_min and i['restaurant']['average_cost_for_two'] < price_max and added <= 5:
						res = res + "\n\nname: "+str(i['restaurant']['location']['address'])+"\naddress :"+str(i['restaurant']['location']['address'])+"\nrating :"+str(i['restaurant']['user_rating']['aggregate_rating'])
						added = added +1

			return "here are the results \n\n "+ res

		else:
			return 0


			


	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		#zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		if loc.lower() not in cities:
			dispatcher.utter_message("We don't operate in your location")
			return [AllSlotsReset()]
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		res = self.fetch(loc,cuisine,price)
		if res == 0:
			dispatcher.utter_message("location is not found")
			return [AllSlotsReset()]
		dispatcher.utter_message(res)
		return [SlotSet('location',loc)]  



# Send email the list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'


	def fetch(self,loc='delhi',cuisine='north indian',price='high'):
		
		#adjust the price range
		price_min = 0
		price_max = 99999
		if price == 'low':
			price_max = 300
		elif price == 'mid':
			price_min = 300
			price_max = 700
		elif price == 'high':
			price_min = 700
		else:
			price_min = 300
			price_max = 9999
		
		# provide API key and initialise a 'zomato app' object
		config={ "user_key": "4734a24a9caf5cd3ae0a0e9161e66212"}
		zomato = zomatopy.initialize_app(config)
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'north':50,'south':85,'indian':80}

		# get_location gets the lat-long coordinates of 'loc'
		loc_detail=zomato.get_location(loc, 1)
		loc_detail=json.loads(loc_detail)
		if loc_detail['status'] == 'success':
			lat = loc_detail['location_suggestions'][0]['latitude']
			lon = loc_detail['location_suggestions'][0]['longitude']
			data =  zomato.restaurant_search( query='', latitude=lat, longitude=lon, cuisines=str(cuisines_dict.get(cuisine)), limit=100)
			data = json.loads(data)
			global res
			if data['results_found'] > 0:
				added=0
				for i in data['restaurants']:
					if i['restaurant']['average_cost_for_two'] > price_min and i['restaurant']['average_cost_for_two'] < price_max and added <= 10:
						res = res + "\n\nname: "+str(i['restaurant']['location']['address'])+"\naddress :"+str(i['restaurant']['location']['address'])+"\nrating :"+str(i['restaurant']['user_rating']['aggregate_rating'])
						added = added +1

				return "here are the results \n\n "+ res
			else:
				return "can't retrive data properly"

		else:
			return "results not found..!!"


			


	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		res = self.fetch(loc,cuisine,price)
		email = tracker.get_slot('email')
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		s.login("gajulajagadeesh7@gmail.com", "something re")
		message = "The details of all the restaurants you inquried \n \n"
		message = message + res
		try:
			s.sendmail("gajulajagadeesh7@gmail.com", str(email), message)
			s.quit()
			dispatcher.utter_message("Email sent please check your inbox. have a nice day")
		except:
			dispatcher.utter_message("Can't send the email. please retry")
			return [AllSlotsReset()]

