import csv

# Create Truck object using info from the LoadTrucks() method
class Truck:
    def __init__(self, truck_id, pkg_list, delivered_list, truck_departure, route_end):
        self.truck_id = truck_id
        self.pkg_list = pkg_list
        self.delivered_list = delivered_list
        self.truck_departure = truck_departure
        self.route_end = route_end

