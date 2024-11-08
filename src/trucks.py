import datetime


# Create the truck class
class Truck:
    def __init__(self, truck_id, pkg_list, delivered_list, truck_departure):
        self.truck_id = truck_id
        self.pkg_list = pkg_list
        self.delivered_list = delivered_list
        self.truck_departure = truck_departure
        self.truck_mileage = 0
        self.truck_time = truck_departure

    # Control what displays when the truck is called
    def __str__(self):
        return 'Truck ID#{}: delivered the following packages today:\n{}\nTruck mileage: {}'.format(
            self.truck_id,
            ', '.join(map(str, self.pkg_list)),
            self.truck_mileage
        )


# Manually loading the trucks with packages and giving them departure times based on package requirements
truck_1 = Truck(
    truck_id=1,
    pkg_list=[1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40],
    delivered_list=[],
    truck_departure=datetime.timedelta(hours=8),
)

# Departure time set to ensure package #6 arrives from airport first
truck_2 = Truck(
    truck_id=2,
    pkg_list=[3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39],
    delivered_list=[],
    truck_departure=datetime.timedelta(hours=9, minutes=5),
)

# Departure time set to ensure package #9 updates address first. Main code has checks to make sure truck has driver
truck_3 = Truck(
    truck_id=3,
    pkg_list=[2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33],
    delivered_list=[],
    truck_departure=datetime.timedelta(hours=10, minutes=20),
)
