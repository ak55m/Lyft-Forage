from datetime import datetime

from tires.all_tires import Tires


class Palindrome(Tires):
    
    #this gives confirmation that one or more tire needs to be serviced
    def tire_needs_service(self):
        
        service_threshold_date = self.last_service_date + datetime.today().date()

        if service_threshold_date < datetime.today().date() and self.tire_should_be_serviced():
            return True
        else:
            return False