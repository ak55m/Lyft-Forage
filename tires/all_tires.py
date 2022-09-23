from abc import ABC

from car import Car


class Tires(Car, ABC):

    def __init__(self, last_service_date, left_front_tire_pressure, right_front_tire_pressure, left_rear_tire_pressure, right_rear_tire_presure):
        super().__init__(last_service_date)
        self.left_front_tire = left_front_tire_pressure
        self.right_front_tire = right_front_tire_pressure
        self.left_rear_tire = left_rear_tire_pressure
        self.right_rear_tire = right_rear_tire_presure

    #this is returns any bool value for when any tire should be serviced
    def tire_should_be_serviced(self):
        if self.left_front_tire < 32:
            return True
        elif self.right_front_tire < 32:
            return True 
        elif self.left_rear_tire < 32:
            return True
        elif self.right_rear_tire < 32:
            return True 
        else:
            return False
