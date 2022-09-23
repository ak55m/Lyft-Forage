from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine):
    
     #this gives confirmation that engine needs to be serviced
    def engine_needs_service(self):

        service_threshold_date = self.last_service_date
        if service_threshold_date < datetime.today().date() and self.engine_should_be_serviced():
            return True
        else:
            return False
y
