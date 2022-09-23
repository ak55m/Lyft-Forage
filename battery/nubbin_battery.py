from abc import ABC

from datetime import datetime

from car import Car


class NubbinBattery(Car, ABC):

    def __init__(self, last_service_date_of_battery, today):
        super().__init__(last_service_date_of_battery)
        self.last_service_date_of_battery = last_service_date_of_battery
        self.today = today

        #convert date to string
        string_of_last_service_date = str(self.last_service_date_of_battery)
        string_of_today_date = str(self.today)

        #convert string to object
        self.obj_last_service_date = datetime.strptime(string_of_last_service_date, "%Y-%m-%d")
        self.obj_today_date = datetime.strptime(string_of_today_date, "%Y-%m-%d")

    #this function returns a bool value for when battery hasn't been service for 4 years
    def battery_should_be_serviced(self):
        return abs(self.obj_last_service_date - self.obj_today_date).days >= 1461