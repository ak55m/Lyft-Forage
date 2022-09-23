from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def engine_needs_service(self):
        pass

    def battery_needs_service(self):
        pass

    def tire_needs_service(self):
        pass
