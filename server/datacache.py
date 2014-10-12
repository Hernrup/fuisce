import requests
import json
import os
import arrow
import base64

class DataCache:
    def __init__(self):
        self.cached_return_json = {}

    def refresh(self):
       print("Refreshing cache")

    def getTastings(self):
       return json.loads('{tastings: [ {id: 1, name: "A"}, {id: 2, name: "B"} ]}')

    def getAllDrinks(self):
       return json.loads('{drinks: [ {id: 1, name: "A"}, {id: 2, name: "B"} ]}')
