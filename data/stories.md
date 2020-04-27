## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "dharmavaramm"}
    - slot{"location": "dharmavaramm"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "banglore"}
    - slot{"location": "banglore"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_prompt
* email{"email": "cherry@gmail.com"}
    - slot{"email": "cherry@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "banglore"}
    - slot{"location": "banglore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "mid", "cuisine": "indian", "location": "banglore"}
    - slot{"cuisine": "indian"}
    - slot{"location": "banglore"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "banglore"}
    - slot{"location": "banglore"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
* affirm
    - utter_email_prompt
* email{"email": "srinivas.soma@gmail.com"}
    - slot{"email": "srinivas.soma@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_prompt
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "mid", "location": "pune"}
    - slot{"location": "pune"}
    - slot{"price": "mid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_email_prompt
    - utter_request_email
* email{"email": "cherryjan96@gmail.com"}
    - slot{"email": "cherryjan96@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "banglore"}
    - slot{"location": "banglore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "howdy@protonmail.com"}
    - slot{"email": "howdy@protonmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* goodbye

## interactive_story_2
* restaurant_search{"price": "low", "cuisine": "american", "location": "banglore"}
    - slot{"cuisine": "american"}
    - slot{"location": "banglore"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "pune", "price": "low"}
    - slot{"location": "pune"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_email_prompt
* affirm
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "banglore", "price": "low", "email": "gajulajagadeesh7@gmail.com"}
    - slot{"cuisine": "chinese"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"location": "banglore"}
    - slot{"price": "low"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* location{"location": "banglore"}
    - slot{"location": "banglore"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "mid", "location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"price": "mid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"val_loc": "True"}
    - utter_email_prompt
    - action_send_email
    - utter_email_prompt
    - utter_request_email

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"val_loc": "True"}
    - utter_email_prompt
* not
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"price": "american"}
    - slot{"price": "american"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"val_loc": "False"}
    - utter_email_prompt
    - utter_email_prompt
    - utter_request_email
* not

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"val_loc": "False"}
    - utter_goodbye
* goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"val_loc": "False"}

## interactive_story_2
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - utter_goodbye
