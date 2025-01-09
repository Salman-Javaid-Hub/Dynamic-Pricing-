import random

class Exogenous:
    def __init__(self):

        self.weather_data = {
            "Rain": 1.2,
            "Snow": 1.15,
            "Thunderstorm": 1.3,
            "Clear": 1.0,
            "Clouds": 1.05,
            "Mist": 1.3,
            "Fog": 1.4,
            "Haze": 1.2,
            "Dust": 1.15,
            "Squall": 1.5,
            "Tornado": 1.7
        }

        self.event_data = {
            "Concert": 1.3,
            "Sports Event": 1.25,
            "Bank Holiday": 1.2,
            "Festival": 1.4,
            "Conference": 1.15,
            "Parade": 1.35,
            "Protest": 1.4,
            "Exhibition": 1.2,
            "None": 1.0
        }

    def weather_calculation(self):
        
        weather = random.choice(list(self.weather_data.keys()))
        w_cost = self.weather_data[weather]
        return weather, w_cost

    def event_calculation(self):
        
        event = random.choice(list(self.event_data.keys()))
        e_cost = self.event_data[event]
        return event, e_cost

