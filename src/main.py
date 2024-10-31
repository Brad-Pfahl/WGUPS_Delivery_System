# Author: Brad Pfahl
# Student ID: 011070820
# Title: C950 WGUPS Routing Program

from src.nearest_neighbor import nearest_neighbor_algorithm
from src.packages import *
from src.trucks import *

# Run package route before Main interface runs so data is available

# Each truck running through algorithm
nearest_neighbor_algorithm(truck_1)
nearest_neighbor_algorithm(truck_2)

# Ensure that the third truck does not leave until one of the drivers returns
truck_3.truck_departure = max(datetime.timedelta(hours=9, minutes=5), min(truck_1.truck_time, truck_2.truck_time))
nearest_neighbor_algorithm(truck_3)

# Take total sum for mileages between trucks
total_mileage = int(truck_1.truck_mileage + truck_2.truck_mileage + truck_3.truck_mileage)


# Functions needed for the interface

def display_menu():
    # User Interface
    print("Western Governors University Parcel Service (WGUPS) Delivery Service")
    print("Please choose an option:")
    print("1. Print All Package Status and Total Mileage")
    print("2. Get a Single Package Status")
    print("3. Get a Single Package Status based on Time")
    print("4. Get All Package Statuses based on Time")
    print("5. Exit the Program")


# View all package status with total mileage. Choice #1
def view_package_status_all():
    print("All Package Statuses with Total Mileage:")
    package_table.print_all()
    print(f"Total Mileage: {total_mileage}")


# Get a single package status. Choice #2
def view_single_package_status(pkg_id):
    pkg_id_int = int(pkg_id)  # Convert string input into integer
    package = package_table.search(pkg_id_int)  # Search for the package by ID

    if package:
        print(f"Package found: {package}")
    else:
        print(f"Package with ID {pkg_id} not found.")


# Get a single package status based on time. Choice #3
def view_single_package_status_based_on_time(pkg_id, time_input):
    print(f"\nPackage Status for ID {pkg_id} at {time_input}:")

    # Convert user input to timedelta
    (h, m, s) = map(int, time_input.split(":"))
    input_time_as_timedelta = datetime.timedelta(hours=h, minutes=m, seconds=s)

    pkg_id_int = int(pkg_id)  # Convert string input into integer
    package = package_table.search(pkg_id_int)  # Search for the package by ID

    if package:
        if package.pkg_delivery_time <= input_time_as_timedelta:
            print(f"Package ID: {package.pkg_id}, Status: Delivered at {package.pkg_delivery_time}.")
        else:
            print(f"Package ID: {package.pkg_id}, Status: {package.pkg_delivery_status}")
    else:
        print(f"Package with ID {pkg_id} not found.")


# Get all package status with a time. Choice # 4
def all_package_status_with_time(time_input):
    print(f"\nPackage Status at {time_input}:")

    # Convert user input to timedelta
    (h, m, s) = map(int, time_input.split(":"))
    input_time_as_timedelta = datetime.timedelta(hours=h, minutes=m, seconds=s)

    for bucket in package_table.table:  # Iterate through the hash table buckets
        for kv in bucket:  # Iterate through each bucket's key-value pairs
            package = kv[1]  # The second element is the package object

            # Check if the package has a delivery time and if it's before or at the specified time
            if package.pkg_delivery_time <= input_time_as_timedelta:
                print(f"Package ID: {package.pkg_id}, Status: Delivered at {package.pkg_delivery_time}.")
            else:
                print(f"Package ID: {package.pkg_id}, Status: {package.pkg_delivery_status}")


# Exit the program. Choice #5
def exit_program():
    print("Exiting the WGUPS delivery system. Hope you had a hoot!")
    exit()


# Main loop to handle user input
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_package_status_all()
        elif choice == '2':
            pkg_id = input("Enter Package ID: ")
            view_single_package_status(pkg_id)
        elif choice == '3':
            pkg_id = input("Enter Package ID: ")
            time_input = input("Enter the time (HH:MM:SS): ")
            view_single_package_status_based_on_time(pkg_id, time_input)
        elif choice == '4':
            time_input = input("Enter the time (HH:MM:SS): ")
            all_package_status_with_time(time_input)
        elif choice == '5':
            exit_program()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
