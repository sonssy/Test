def change_km_to_mile(km):
    return km*0.621371

def change_mile_to_km(mile):
    return mile*1.609344

class Car:
    def __init__(self):
        self._speed=0
    def get_speed(self):
        return self._speed
    def start(self):
        self._speed=20
    def accelerate(self):
        self._speed=self._speed+30
    def stop(self):
        self._speed=0

class Truck:
    def __init__(self):
        self._speed=0
    def get_speed(self):
        return self._speed
    def start(self):
        self._speed=10
    def accelerate(self):
        self._speed=self._speed+20
    def stop(self):
        self._speed=0