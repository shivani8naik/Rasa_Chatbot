# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
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

# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTeachPythonConcept(Action):
    def name(self) -> Text:
        return "action_teach_python_concept"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        concept = tracker.latest_message['intent'].get('name')

        if concept == 'ask_variables':
            explanation = "In Python, variables are used to store data. You can assign values to variables like this: `variable_name = value`. For example, `name = 'John'`."
        
        elif concept == 'ask_data_types':
            explanation = "Python 3 supports several built-in data types, including integers, floats, strings, booleans, lists, tuples, and dictionaries."

        elif concept == 'ask_operators':
            explanation = "Python 3 supports a variety of operators, including arithmetic operators (+, -, *, /), comparison operators (>, <, ==, !=), and logical operators (and, or, not)."
        
        elif concept == 'ask_control_flow_statements':
            explanation = "Python 3 supports several control flow statements, including if-else statements, for loops, and while loops. These statements allow you to control the flow of execution in your code."
        
        elif concept == 'ask_loops':
            explanation = "Loops in Python allow you to repeat a block of code multiple times. The two main types are 'for' and 'while' loops. For example, a 'for' loop can be used to iterate over a list of items."
        
        elif concept == 'ask_functions':
            explanation = "In Python 3, functions are created using the def keyword. For example, def my_function(x): creates a function called my_function that takes one argument called x."
        
        else:
            explanation = "I'm still learning about that concept. Let's try another topic."

        dispatcher.utter_message(text=explanation)
        return []
