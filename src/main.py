# Author: Brad Pfahl
# Student ID: 011070820
# Title: C950 WGUPS Routing Program
import datetime

from src.nearest_neighbor import nearest_neighbor_algorithm
from src.packages import *
from src.trucks import truck_1, truck_2, truck_3

# Each truck running through algorithm
nearest_neighbor_algorithm(truck_1)
nearest_neighbor_algorithm(truck_2)

# Ensure that truck 3 does not leave until one of the drivers returns, and we know the correct address for pkg 9
truck_3.truck_departure = max(datetime.timedelta(hours=10, minutes=20), min(truck_1.truck_time, truck_2.truck_time))
nearest_neighbor_algorithm(truck_3)

# Calculate total mileage after all trucks complete their routes
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
                print(f"Package ID: {package.pkg_id}"
                      f"; Status: {package.pkg_delivery_status} at {package.pkg_delivery_time}"
                      f"; Delivery Deadline: {package.pkg_deadline}"
                      f"; Delivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                      f"; {package.pkg_zip}."
                      f"; Weight: {package.pkg_weight}")


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
            print(f"Package ID: {package.pkg_id}"
                  f"; Status: {package.pkg_delivery_status} at {package.pkg_delivery_time}"
                  f"; Delivery Deadline: {package.pkg_deadline}"
                  f"; Delivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                  f"; {package.pkg_zip}."
                  f"; Weight: {package.pkg_weight}")
        else:
            print(f"Package ID: {package.pkg_id}"
                  f"; Status: {package.pkg_delivery_status}"
                  f"; Delivery Deadline: {package.pkg_deadline}"
                  f"; Delivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                  f"; {package.pkg_zip}."
                  f"; Weight: {package.pkg_weight}")
    else:
        print(f"Package with ID {pkg_id} not found.")


# Get all package status with a time. Choice # 4
def all_package_status_with_time(time_input):
    print(f"\nPackage Status at {time_input}:")

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
                    print(f"Package ID: {package.pkg_id}"
                          f"; Status: {package.pkg_delivery_status} at {package.pkg_delivery_time}"
                          f"; Delivery Deadline: {package.pkg_deadline}"
                          f"; Delivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                          f"; {package.pkg_zip}."
                          f"; Weight: {package.pkg_weight}")
                else:
                    print(f"Package ID: {package.pkg_id}"
                          f"; Status: {package.pkg_delivery_status}"
                          f"; Delivery Deadline: {package.pkg_deadline}"
                          f"; Delivery Address: {package.pkg_address} {package.pkg_city}, {package.pkg_state}"
                          f"; {package.pkg_zip}."
                          f"; Weight: {package.pkg_weight}")


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


# Main loop to handle user input
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        # Print All Package Status and Total Mileage
        if choice == '1':
            view_package_status_all()

        # Get a Single Package Status
        elif choice == '2':
            try:
                pkg_id = input("Enter Package ID: ")
                pkg_id_int = int(pkg_id)  # Attempt to convert to integer
                view_single_package_status(pkg_id_int)
            except ValueError:
                print("Invalid input! Please enter a numerical Package ID.")

        # Get a Single Package Status Based on Time
        elif choice == '3':
            try:
                pkg_id = input("Enter Package ID: ")
                pkg_id_int = int(pkg_id)  # Attempt to convert to integer

                time_input = input("Enter the time (HH:MM:SS): ")
                (h, m, s) = map(int, time_input.split(":"))  # Convert time to integers
                view_single_package_status_based_on_time(pkg_id_int, time_input)
            except ValueError:
                print("Invalid input! Please enter the Package ID as a number and time as HH:MM:SS.")

        # Get All Package Statuses based on Time
        elif choice == '4':
            try:
                time_input = input("Enter the time (HH:MM:SS): ")
                (h, m, s) = map(int, time_input.split(":"))  # Convert time to integers
                all_package_status_with_time(time_input)
            except ValueError:
                print("Invalid time format! Please enter the time as HH:MM:SS.")

        # Get Truck Details based on Truck Number
        elif choice == '5':
            try:
                truck_input = input("Enter the truck ID (1-3): ")
                display_truck_details(truck_input)
            except ValueError:
                print("Invalid input! Please enter a valid truck.")

        # Exit
        elif choice == '6':
            exit_program()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
