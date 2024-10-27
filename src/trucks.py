import datetime

from src.packages import package_table


# Create Truck object using info from the LoadTrucks() method
class Truck:
    def __init__(self, truck_id, pkg_list, delivered_list, truck_departure, truck_mileage, truck_time):
        self.truck_id = truck_id
        self.pkg_list = pkg_list
        self.delivered_list = delivered_list
        self.truck_departure = truck_departure
        self.truck_mileage = 0
        self.truck_time = truck_time

    # Control what displays when the truck is called
    def __str__(self):
        return 'Truck ID: {} delivered the following packages today:\n{}'.format(self.truck_id,
                                                                                 ', '.join(map(str, self.pkg_list)))


# Manually loading the trucks
truck_0 = Truck(0, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], [], datetime.timedelta(hours=8), 0,
                datetime.timedelta(hours=8))

truck_1 = Truck(1, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], [],
                datetime.timedelta(hours=10, minutes=30), 0, datetime.timedelta(hours=8))

truck_2 = Truck(2, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], [], datetime.timedelta(hours=9, minutes=5), 0,
                datetime.timedelta(hours=8))

truck_2.truck_departure = max(datetime.timedelta(hours=9, minutes=5), min(truck_0.truck_time, truck_1.truck_time))