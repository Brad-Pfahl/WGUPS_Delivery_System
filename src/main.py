# Author: Brad Pfahl
# Student ID: 011070820
# Title: C950 WGUPS Routing Program
from src.dijkstra import dijkstraAlgorithmShortestPath
from src.hashtable import ChainingHashTable
from src.packages import *
from src.trucks import truck_0
from src.distance import *
from src.trucks import *

dijkstraAlgorithmShortestPath(truck_0)
dijkstraAlgorithmShortestPath(truck_1)
truck_2.truck_departure = max(datetime.timedelta(hours=9, minutes=5), min(truck_0.truck_time, truck_1.truck_time))
dijkstraAlgorithmShortestPath(truck_2)

total_mileage = int(truck_0.truck_mileage + truck_1.truck_mileage + truck_2.truck_mileage)
print(total_mileage)

package = package_table.search(18)
if package:
    print(f"Package found: {package}")
else:
    print("Package not found.")

print(truck_0.truck_time, truck_1.truck_time, truck_2.truck_time)


# Functions needed for the interface

def display_menu():
    # User Interface
    print("Western Governors University Parcel Service (WGUPS) Delivery Service")
    print("Please choose an option:")
    print("1. Print All Package Status and Total Mileage")
    print("2. Get a Single Package Status with a Time")
    print("3. Get All Package Status with a Time")
    print("4. Exit the Program")


# View all package status with total mileage
def view_package_status_all():
    print("All Package Statuses with Total Mileage:")
    package_table.print_all()
    print(f"Total Mileage: {total_mileage}")


# Get a single package status
def view_single_package_status(pkg_id):
    package = package_table.search(pkg_id)  # Search for the package by ID

    if package:
        print(f"Package found: {package}")
    else:
        print(f"Package with ID {pkg_id} not found.")


# Get all package status with a time
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
                print(f"Package ID: {package.pkg_id}, Status: In Transit or Not Yet Departed.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(view_package_status_all())
            pass

        elif choice == '2':
            pkg_id = input("Enter the package ID: ")
            view_single_package_status(pkg_id)
            pass

        elif choice == '3':
            time_input = input(
                "Please enter a time to check the status of package(s). Use the following format, HH:MM:SS: ")
            try:
                all_package_status_with_time(time_input)  # Call function to display package statuses
            except ValueError:
                print("Invalid time format. Please use HH:MM:SS format.")

        elif choice == '4':
            print("Exiting the program.")
            break  # Exit the loop and program

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
