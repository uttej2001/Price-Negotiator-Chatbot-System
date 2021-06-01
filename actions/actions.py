# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from typing_extensions import IntVar

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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

class ActionShowProductAvailable(Action):

     def name(self) -> Text:
         return "action_product_list"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'product':
                 name = e['value']

             if name == "bikes":
                 message = "We have Touring Bikes,Road Bikes,Mountain Bikes.See anything you like?Just ask it."

             if name == "accessories":
                 message = "We have Belts,Caps,Ties.See anything you like?Just ask it."

             if name == "fashion":
                 message = "We have Vintage fashion style,Casual clothes,Formal clothes.See anything you prefer?Just ask it."

         dispatcher.utter_message(message)

         return []

class ActionBikes(Action):

     def name(self) -> Text:
         return "action_bikes"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'bikes':
                 name = e['value']

             if name == "touring":
                 message = "We have KTM 390 Duke, Royal Enfield Himalayan"

             if name == "road":
                 message = "We have Race bikes, Aero bikes"

             if name == "mountain":
                 message = "We have Trail bikes, Downhill bikes"

         dispatcher.utter_message(text=message)

         return []

class ActionTouring(Action):

     def name(self) -> Text:
         return "action_touring"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'touring':
                 name = e['value']

             if name == "KTM":
                 message = "https://cutt.ly/HnpIx7O"

             if name == "Royal Enfield":
                 message = "https://cutt.ly/snpIbRF"

         dispatcher.utter_message(message)

         return []

class ActionRoad(Action):

     def name(self) -> Text:
         return "action_road"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'road':
                 name = e['value']

             if name == "race":
                 message = "https://cutt.ly/3npIFjD"

             if name == "areo":
                 message = "https://cutt.ly/JnpIRrU"

         dispatcher.utter_message(message)

         return []

class ActionMountain(Action):

     def name(self) -> Text:
         return "action_mountain"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'mountain':
                 name = e['value']

             if name == "trail":
                 message = "https://cutt.ly/SnpIX3D"

             if name == "downhill":
                 message = "https://cutt.ly/lnpILl3"

         dispatcher.utter_message(message)

         return []         

class ActionAccessories(Action):

     def name(self) -> Text:
         return "action_accessories"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'accessories':
                 name = e['value']

             if name == "belts":
                 message = "We have Buckle belt, Metal belts"

             if name == "caps":
                 message = "We have Baseball Caps, Fedora Caps"

             if name == "ties":
                 message = "We have Novelty Ties, Solid Ties"
         dispatcher.utter_message(message)

         return []

class ActionBelts(Action):

     def name(self) -> Text:
         return "action_belts"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'belts':
                 name = e['value']

             if name == "metal":
                 message = "https://cutt.ly/Bnorn2J"

             if name == "buckle":
                 message = "https://cutt.ly/HnorQzT"

         dispatcher.utter_message(message)

         return []

class ActionTies(Action):

     def name(self) -> Text:
         return "action_ties"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'ties':
                 name = e['value']

             if name == "novelty":
                 message = "https://cutt.ly/znorXZq"

             if name == "solid":
                 message = "https://cutt.ly/Enor2y0"

         dispatcher.utter_message(message)

         return []

class ActionCaps(Action):

     def name(self) -> Text:
         return "action_caps"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'caps':
                 name = e['value']

             if name == "baseball":
                 message = "https://cutt.ly/8norpFm"

             if name == "fedora":
                 message = "https://cutt.ly/6norxFX"

         dispatcher.utter_message(message)

         return []

class ActionFashion(Action):

     def name(self) -> Text:
         return "action_fashion"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'fashion':
                 name = e['value']

             if name == "vintage":
                 message = "We have Flared Jeans, Granny Glasses"

             if name == "casual":
                 message = "We have Minidress, Shorts"

             if name == "formal":
                 message = "We have Formal Shirts, Formal Jeans"
         dispatcher.utter_message(message)

         return []

class ActionVintageStyle(Action):

     def name(self) -> Text:
         return "action_vintage"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'vintage':
                 name = e['value']

             if name == "flared jeans":
                 message = "https://cutt.ly/mnoa0vG"

             if name == "granny glasses":
                 message = "https://cutt.ly/cnosety"

         dispatcher.utter_message(message)

         return []

class ActionCasualClothes(Action):

     def name(self) -> Text:
         return "action_casual"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'casual':
                 name = e['value']

             if name == "minidress":
                 message = "https://cutt.ly/wnoszmv"

             if name == "shorts":
                 message = "https://cutt.ly/gnosnfn"

         dispatcher.utter_message(message)

         return []

class ActionFormalClothes(Action):

     def name(self) -> Text:
         return "action_formal"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'formal':
                 name = e['value']

             if name == "shirts":
                 message = "https://cutt.ly/rnosOQr"

             if name == "jeans":
                 message = "https://cutt.ly/knosS6m"

         dispatcher.utter_message(message)

         return []

class ActionDiscountOffer(Action):

     def name(self) -> Text:
         return "action_discount_offer"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'discount_offer':
                 name = e['value']

             if name == "discount":
                 message = "You will have 3 chances to enter discount percentage. If you are lucky you can get discount upto 50%"

             if name == "offer":
                 message = "You will have 3 chances to enter discount percentage. If you are lucky you can get this product for 50% off"

             if name == "last":
                 message = "You will have 3 chances to enter discount percentage.First let's begin the negotiations."

         dispatcher.utter_message(message)

         return []

class ActionDiscount(Action):

     def name(self) -> Text:
         return "action_discount"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'discount':
                 discount1 = e['value']
             discount1 = int(discount1)
             if (discount1 <= 10):
                 bot_discount1 = (discount1)
                 bot_discount1 = int(bot_discount1)
                 print("final discount: ",bot_discount1)
                 message = "Seems reasonable, We have a deal! You can purchase this product for discount of {}%".format(bot_discount1)         
             if (10 < discount1 <= 100):
                 bot_discount1 = (discount1)*0.6
                 bot_discount1 = int(bot_discount1)
                 print("final discount: ",bot_discount1)
                 message = "That's too much to ask! How about discount of {}%".format(bot_discount1)
         dispatcher.utter_message(message)

         return []

class ActionOffer(Action):

     def name(self) -> Text:
         return "action_offer"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'offer':
                 discount2 = e['value']
             discount2 = int(discount2)
             if (discount2 <= 10):
                 bot_discount2 = (discount2)
                 bot_discount2 = int(bot_discount2)
                 print("final discount: ",bot_discount2)
                 message = "Seems reasonable, We have a deal! You can purchase this product for discount of {}%".format(bot_discount2)         
             if (10 < discount2 <= 100):
                 bot_discount2 = (discount2)*0.75
                 bot_discount2 = int(bot_discount2)
                 print("final discount: ",bot_discount2)
                 message = "It's still slightly high! How about {}% off".format(bot_discount2)
         dispatcher.utter_message(message)

         return []

class ActionLast(Action):

     def name(self) -> Text:
         return "action_last"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'last':
                 discount3 = e['value']
             discount3 = int(discount3)
             if (discount3 <= 10):
                 bot_discount3 = (discount3)
                 bot_discount3 = int(bot_discount3)
                 print("final discount: ",bot_discount3)
                 message = "Seems reasonable, We have a deal! You can purchase this product for discount of {}%".format(bot_discount3)         
             if (10 < discount3 <= 100):
                 bot_discount3 = (discount3)*0.90
                 bot_discount3 = int(bot_discount3)
                 print("final discount: ",bot_discount3)
                 message = "Okay let's make it our last deal! How about {}% off".format(bot_discount3)
         dispatcher.utter_message(message)

         return []
