import csv
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
        self.pkg_delivery_status = 'Processing'
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
