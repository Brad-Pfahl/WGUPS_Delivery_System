import datetime

from src.distance import distance_between
from src.packages import package_table


# This is our main routing algorithm based on the nearest neighbor algorithm
def nearest_neighbor_algorithm(truck):
    # Create a list of packages to be delivered
    package_list = truck.pkg_list[:]
    hub_address = "4001 South 700 East"

    # Start from the hub
    current_address = hub_address
    total_mileage = 0
    delivery_time = truck.truck_departure

    # Track the delivery order of packages
    delivery_order = []

    # Update package departure times
    for pkg_id in package_list:
        package = package_table.search(pkg_id)
        if package:
            package.pkg_departure_time = truck.truck_departure

    while package_list:
        # Update package addresses based on current time
        current_time = delivery_time
        for pkg_id in package_list:
            package = package_table.search(pkg_id)
            if package:
                package.address_update(current_time)  # Call the update method

        # Find the nearest package
        nearest_package = None
        nearest_distance = float('inf')

        for pkg_id in package_list:
            package = package_table.search(pkg_id)
            if package:
                distance = distance_between(current_address, package.pkg_address)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_package = package

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
