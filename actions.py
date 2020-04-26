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


res=''
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		city_obj = cities.city_class()
		city_list = city_obj.top_city()
		if loc.lower() not in city_list:
			dispatcher.utter_message("Sorry we are not serving in this location")
			return []
		location_detail=zomato.get_location(loc,1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"

		res = response
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]



# Send email the list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')
		

		import smtplib 
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		s.login("gajulajagadeesh7@gmail.com", "something")
		message = "The details of all the restaurants you inquried \n \n"
		global res
		message = message + res
		try:
			s.sendmail("gajulajagadeesh7@gmail.com", str(email), message)
			s.quit()
		except:
			dispatcher.utter_message(email)

		return [AllSlotsReset()]

