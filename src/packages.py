import csv
import datetime

import hashtable


# Create the package class
class Package:
    def __init__(self, pkg_id, pkg_address, pkg_city, pkg_state, pkg_zip, pkg_deadline, pkg_delivery_status,
                 pkg_departure_time, pkg_delivery_time, pkg_weight, pkg_special_notes):
        self.pkg_id = int(pkg_id)
        self.pkg_address = pkg_address
        self.pkg_city = pkg_city
        self.pkg_state = pkg_state
        self.pkg_zip = pkg_zip
        self.pkg_deadline = pkg_deadline
        self.pkg_delivery_status = 'At the Hub'
        self.pkg_departure_time = None
        self.pkg_delivery_time = None
        self.pkg_weight = pkg_weight
        self.pkg_special_notes = pkg_special_notes

    # Identify what the package will show when called
    def __str__(self):
        return ('Package ID: %s\n'
                'Package Delivery Address: %s, %s %s, %s\n'
                'Delivery Deadline: %s\n'
                'Delivery Status: %s\n'
                'Delivered ''at: ''%s\n'
                'Package weight: %s\n'
                'Special Conditions (if available): %s') % (
            self.pkg_id, self.pkg_address, self.pkg_city, self.pkg_state, self.pkg_zip,
            self.pkg_deadline, self.pkg_delivery_status, self.pkg_delivery_time, self.pkg_weight, self.pkg_special_notes)

    # Update the address for package #9 if the time is at or past 10:20
    def address_update(self, current_time):
        if self.pkg_id == 9:
            correction_time = datetime.timedelta(hours=10, minutes=20)
            if current_time >= correction_time:
                self.pkg_address = "410 S State St"
                self.pkg_city = "Salt Lake City"
                self.pkg_state = "UT"
                self.pkg_zip = "84111"
            else:
                self.pkg_address = "300 State St"
                self.pkg_city = "Salt Lake City"
                self.pkg_state = "UT"
                self.pkg_zip = "84103"

    def update_status(self, convert_timedelta):
        self.address_update(convert_timedelta)  # Update address first

        # Check delivery status based on current time
        if self.pkg_delivery_time and self.pkg_delivery_time <= convert_timedelta:
            self.pkg_delivery_status = "Delivered"
        elif self.pkg_departure_time and self.pkg_departure_time <= convert_timedelta:
            self.pkg_delivery_status = "En Route"
        else:
            self.pkg_delivery_status = "At the Hub"


# Create new instance of ChainingHashTable
package_table = hashtable.ChainingHashTable()

# Read the packages from the CSV file
pkg_file = open('csvs/WGUPS_Packages.csv')
pkg_dict_reader = csv.DictReader(pkg_file, ['Package_ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight',
                                            'Special_Notes'])
# Load each package into the hash table
for row in pkg_dict_reader:
    package = Package(
        pkg_id=row['Package_ID'],
        pkg_address=row['Address'],
        pkg_city=row['City'],
        pkg_state=row['State'],
        pkg_zip=row['Zip'],
        pkg_deadline=row['Deadline'],
        pkg_delivery_status=None,
        pkg_departure_time=None,
        pkg_delivery_time=None,
        pkg_weight=row['Weight'],
        pkg_special_notes=row['Special_Notes']
    )

    # Insert the package into the hash table while using the ID as the key and the package as the item
    package_table.insert(package.pkg_id, package)

# Used during testing to make sure packages are being loaded correctly, commented out when not in use
'''
package = package_table.search(18)
if package:
    print(f"Package found: {package}")
else:
    print("Package not found.")
'''
