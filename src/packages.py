import csv

# Create the package class
class Package:
    def __init__(self, pkg_id, pkg_address, pkg_city, pkg_state, pkg_zip, pkg_deadline, pkg_weight, pkg_special_notes):
        self.pkg_id = pkg_id
        self.pkg_address = pkg_address
        self.pkg_city = pkg_city
        self.pkg_state = pkg_state
        self.pkg_zip = pkg_zip
        self.pkg_deadline = pkg_deadline
        self.pkg_weight = pkg_weight
        self.pkg_special_notes = pkg_special_notes


pkg_file = open('csvs/WGUPS_Packages.csv')
pkg_dict_reader = csv.DictReader(pkg_file, ['Package_ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight', 'Special_Notes'])
for row in pkg_dict_reader:
    print(row['Package_ID'], row['Address'], row['City'], row['State'], row['Zip'], row['Deadline'], row['Weight'], row['Special_Notes'])
