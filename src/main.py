# Author: Brad Pfahl
# Student ID: 011070820
# Title: C950 WGUPS Routing Program

from src.interface import *
from src.nearest_neighbor import run_nearest_neighbor_algorithm


# Main loop to handle user input
def main():
    while True:
        # Run package route before everything so data is available
        run_nearest_neighbor_algorithm()
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            view_package_status_all()

        elif choice == '2':
            try:
                pkg_id = input("Enter Package ID: ")
                pkg_id_int = int(pkg_id)  # Attempt to convert to integer
                view_single_package_status(pkg_id_int)
            except ValueError:
                print("Invalid input! Please enter a numerical Package ID.")

        elif choice == '3':
            try:
                pkg_id = input("Enter Package ID: ")
                pkg_id_int = int(pkg_id)  # Attempt to convert to integer

                time_input = input("Enter the time (HH:MM:SS): ")
                (h, m, s) = map(int, time_input.split(":"))  # Convert time to integers
                view_single_package_status_based_on_time(pkg_id_int, time_input)
            except ValueError:
                print("Invalid input! Please enter the Package ID as a number and time as HH:MM:SS.")

        elif choice == '4':
            try:
                time_input = input("Enter the time (HH:MM:SS): ")
                (h, m, s) = map(int, time_input.split(":"))  # Convert time to integers
                all_package_status_with_time(time_input)
            except ValueError:
                print("Invalid time format! Please enter the time as HH:MM:SS.")

        elif choice == '5':
            try:
                truck_input = input("Enter the truck ID (1-3): ")
                display_truck_details(truck_input)
            except ValueError:
                print("Invalid input! Please enter a valid truck.")

        elif choice == '6':
            exit_program()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
