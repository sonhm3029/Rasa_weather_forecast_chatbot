# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from service.weather import get_text_weather_date
from service.normalization import text_to_date, text_to_coordinate


class ActionWeatherFormSubmit(Action):
    def name(self) -> Text:
        return "action_weather_form_submit"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        city = tracker.get_slot("address")
        date_next = tracker.get_slot("date-time")
        date_object = text_to_date(date_next)
        
        if not date_object:
            msg = f"Not support weather query for {city} {date_next}"
            dispatcher.utter_message(msg)
        else:
            dispatcher.utter_message(template="utter_working_on_it")
            
            try:
                lat, lon = text_to_coordinate(city)
                weather_data = get_text_weather_date(lat, lon, date_object, date_next, city)
            except Exception as e:
                exec_msg = str(e)
                dispatcher.utter_message(exec_msg)
            else:
                dispatcher.utter_message(weather_data)
            
        return []