from datetime import datetime

from battery.nubbin_battery import NubbinBattery


class Rorschach(NubbinBattery):
    
    #this gives confirmation that the battery needs to be serviced
    def battery_needs_service(self):

        service_threshold_date = self.last_service_date

        if service_threshold_date < datetime.today().date() and self.battery_should_be_serviced():
            return True
        else:
            return False