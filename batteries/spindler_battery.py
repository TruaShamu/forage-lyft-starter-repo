from abc import ABC
from dateutil import relativedelta

from batteries.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        diff = relativedelta(self.current_date, self.last_service_date)
        return (diff.years >= 3)