# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionWeatherFormSubmit(Action):
    def name(self) -> Text:
        return "action_weather_form_submit"
    
    def run(self, dispatch, tracker, domain):
        city = tracker.get_slot("address")
        date_text = tracker.get_slot("date-time")
        date_object = text_to
