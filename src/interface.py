import datetime

from src.nearest_neighbor import nearest_neighbor_algorithm
from src.packages import *
from src.trucks import truck_1, truck_2, truck_3

# Take total sum for mileages between trucks
total_mileage = int(truck_1.truck_mileage + truck_2.truck_mileage + truck_3.truck_mileage)


# Functions needed for the interface

def display_menu():
    # User Interface
    print("\nWestern Governors University Parcel Service (WGUPS) Delivery Service")
    print("Please choose an option:")
    print("\n1. Print All Package Status and Total Mileage")
    print("2. Get a Single Package Status")
    print("3. Get a Single Package Status based on Time")
    print("4. Get All Package Statuses based on Time")
    print("5. Get Truck Details based on Truck Number")
    print("6. Exit the Program")


# View all package status with total mileage. Choice #1
def view_package_status_all():
    print("All Package Statuses with Total Mileage:")
    # Print the total mileage of all trucks combined
    print(f"\nTotal Mileage: {total_mileage}")

    # For each truck, display its packages
    for truck in [truck_1, truck_2, truck_3]:  # Loop through each truck
        print(f"\nTruck {truck.truck_id} Packages:")

        for pkg_id in truck.pkg_list:  # Loop through the packages assigned to this truck
            package = package_table.search(pkg_id)  # Look up the package by ID
            if package:
                print(f"\nPackage ID: {package.pkg_id}"
                      f"\nStatus: {package.pkg_delivery_status} at {package.pkg_delivery_time}"
                      f"\nDelivery Deadline: {package.pkg_deadline}"
                      f"\nDelivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                      f", {package.pkg_zip}."
                      f"\nWeight: {package.pkg_weight}")


# Get a single package status. Choice #2
def view_single_package_status(pkg_id):
    package = package_table.search(pkg_id)  # Search for the package by ID

    if package:
        print(f"\nPackage found:\n{package}")
    else:
        print(f"Package with ID {pkg_id} not found.")


# Get a single package status based on time. Choice #3
def view_single_package_status_based_on_time(pkg_id, time_input):
    print(f"\nPackage Status for ID {pkg_id} at {time_input}:")

    # Convert user input to timedelta
    (h, m, s) = map(int, time_input.split(":"))
    convert_timedelta = datetime.timedelta(hours=h, minutes=m, seconds=s)

    package = package_table.search(pkg_id)  # Search for the package by ID

    if package:
        package.update_status(convert_timedelta)
        if package.pkg_delivery_time <= convert_timedelta:
            print(f"\nPackage ID: {package.pkg_id}"
                  f"\nStatus: {package.pkg_delivery_status} at {package.pkg_delivery_time}"
                  f"\nDelivery Deadline: {package.pkg_deadline}"
                  f"\nDelivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                  f", {package.pkg_zip}."
                  f"\nWeight: {package.pkg_weight}")
        else:
            print(f"\nPackage ID: {package.pkg_id}"
                  f"\nStatus: {package.pkg_delivery_status}"
                  f"\nDelivery Deadline: {package.pkg_deadline}"
                  f"\nDelivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                  f", {package.pkg_zip}."
                  f"\nWeight: {package.pkg_weight}")
    else:
        print(f"Package with ID {pkg_id} not found.")


# Get all package status with a time. Choice # 4
def all_package_status_with_time(time_input):
    print(f"\nPackage Status at {time_input}:")
    print(f"Total Mileage: {total_mileage}")

    # Convert user input to timedelta
    (h, m, s) = map(int, time_input.split(":"))
    convert_timedelta = datetime.timedelta(hours=h, minutes=m, seconds=s)

    for truck in [truck_1, truck_2, truck_3]:  # Loop through each truck
        print(f"\nTruck {truck.truck_id} Packages at {time_input}:")

        for pkg_id in truck.pkg_list:  # Loop through the packages assigned to this truck
            package = package_table.search(pkg_id)  # Look up the package by ID
            if package:
                package.update_status(convert_timedelta)
                if package.pkg_delivery_time <= convert_timedelta:
                    print(f"\nPackage ID: {package.pkg_id}"
                          f"\nStatus: {package.pkg_delivery_status} at {package.pkg_delivery_time}"
                          f"\nDelivery Deadline: {package.pkg_deadline}"
                          f"\nDelivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                          f", {package.pkg_zip}."
                          f"\nWeight: {package.pkg_weight}")
                else:
                    print(f"\nPackage ID: {package.pkg_id}"
                          f"\nStatus: {package.pkg_delivery_status}"
                          f"\nDelivery Deadline: {package.pkg_deadline}"
                          f"\nDelivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                          f", {package.pkg_zip}."
                          f"\nWeight: {package.pkg_weight}")


# View truck details. Choice # 5
def display_truck_details(truck):
    # Displays the details of the specified truck.
    if truck == "1":
        print(f"{truck_1}")
    elif truck == "2":
        print(f"{truck_2}")
    elif truck == "3":
        print(f"{truck_3}")
    else:
        print(f"Truck number {truck} not found. Please enter 1-3")


# Exit the program. Choice #6
def exit_program():
    print("Exiting the WGUPS delivery system. Hope you had a hoot!")
    exit()
