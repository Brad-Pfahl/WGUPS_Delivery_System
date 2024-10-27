import datetime

from src.distance import addressData, distanceData, distance_between
from src.packages import package_table
from src.trucks import truck_0, truck_1, truck_2, Truck


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

    # Set the packages to In Transit when truck departs
    for pkg_id in package_list:
        package = package_table.search(pkg_id)
        if package:
            package.pkg_delivery_status = "In Transit"

    while package_list:
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

        # Update the package's delivery status and time
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

    # Print delivery summary
    print(f"\nTruck {truck.truck_id} completed deliveries:")
    print(f"Total Mileage: {total_mileage:.1f} miles")
    print(f"Final Delivery Time: {delivery_time}")

    for pkg_id in delivery_order:
        package = package_table.search(pkg_id)
        print(f"Delivered package {pkg_id} to {package.pkg_address} at {package.pkg_delivery_time}.")


# Example usage
# Call this function for each truck
nearest_neighbor_algorithm(truck_0)
nearest_neighbor_algorithm(truck_1)
truck_2.truck_departure = max(datetime.timedelta(hours=9, minutes=5), min(truck_0.truck_time, truck_1.truck_time))
nearest_neighbor_algorithm(truck_2)

total_mileage = int(truck_0.truck_mileage + truck_1.truck_mileage + truck_2.truck_mileage)
print(total_mileage)

