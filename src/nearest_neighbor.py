import datetime

from src.distance import distance_between
from src.packages import package_table
from src.trucks import truck_1, truck_3, truck_2


# This is our main routing algorithm based on the nearest neighbor algorithm
def nearest_neighbor_algorithm(truck):
    # Create a list of packages to be delivered
    package_list = truck.pkg_list[:]
    hub_address = "4001 South 700 East"

    # Start from the hub
    current_address = hub_address
    total_mileage = 0  # Initialize mileage to 0
    delivery_time = truck.truck_departure

    # Track the delivery order of packages
    delivery_order = []

    # Update package departure times
    for pkg_id in package_list:
        package = package_table.search(pkg_id)
        if package:
            package.pkg_departure_time = truck.truck_departure

    # Continue delivering packages until the package list is empty
    while package_list:
        # Update package addresses based on current time. This is useful for status updates
        current_time = delivery_time
        for pkg_id in package_list:
            package = package_table.search(pkg_id)
            if package:
                package.address_update(current_time)  # Call the update method to refresh address details

        # Initialize variables to find the nearest package
        nearest_package = None
        nearest_distance = float('inf')  # Start with infinite distance

        # Loop through all packages to find the nearest one
        for pkg_id in package_list:
            package = package_table.search(pkg_id)  # Look up each package
            if package:
                # Calculate the distance from the current address to the package's address
                distance = distance_between(current_address, package.pkg_address)
                if distance < nearest_distance:  # Check if this package is closer than previously found
                    nearest_distance = distance  # Update nearest distance
                    nearest_package = package  # Update the nearest package reference

        # Update total mileage
        total_mileage += nearest_distance

        # Calculate delivery time and update package status
        time_to_deliver = nearest_distance / 18  # Speed = 18 miles/hour
        delivery_time += datetime.timedelta(hours=time_to_deliver)

        # Update the nearest package's delivery time and status to "Delivered"
        if nearest_package:
            nearest_package.pkg_delivery_time = delivery_time
            nearest_package.pkg_delivery_status = "Delivered"
            delivery_order.append(nearest_package.pkg_id)

            # Update current address to the delivered package's address
            current_address = nearest_package.pkg_address

            # Remove the delivered package from the list
            package_list.remove(nearest_package.pkg_id)

    # Return to the hub after delivering all packages
    # This makes sure that the third truck does not leave until one of the drivers returns
    return_distance = distance_between(current_address, hub_address)
    total_mileage += return_distance
    delivery_time += datetime.timedelta(hours=return_distance / 18)  # Return trip time

    # Update truck details
    truck.truck_mileage = total_mileage
    truck.truck_time = delivery_time


# Routing algorithm function for each truck with special departure time fo truck 3
def run_nearest_neighbor_algorithm():
    # Each truck running through algorithm
    nearest_neighbor_algorithm(truck_1)
    nearest_neighbor_algorithm(truck_2)

    # Ensure that truck 3 does not leave until one of the drivers returns, and we know the correct address for pkg 9
    truck_3.truck_departure = max(datetime.timedelta(hours=10, minutes=20), min(truck_1.truck_time, truck_2.truck_time))
    nearest_neighbor_algorithm(truck_3)
