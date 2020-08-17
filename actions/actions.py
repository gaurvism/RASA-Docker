# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import re

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionTicketCreation(FormAction):

    def name(self) -> Text:
        return "helpdesk_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["name", "domain", "email", "userId", "location", "browser"]

    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate name value."""

        if re.match("^[A-Za-z]*$", value):
            if 2 < len(value) < 50:
                # validation succeeded, set the value of the "name" slot to value
                return {"name": value}
            else:
                dispatcher.utter_message(template="utter_name_range")
                # validation failed, set this slot to None, meaning the
                # user will be asked for the slot again
                return {"name": None}
        else:
            dispatcher.utter_message(template="utter_invalid_name")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"name": None}

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email value."""

        if re.match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", value):
            return {"email": value}
        else:
            dispatcher.utter_message(template="utter_invalid_email")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"email": None}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message(template="utter_slots_value")

        return []
