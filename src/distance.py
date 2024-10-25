import csv

# Read address data from WGUPS_Addresses.csv
addressData = []
with open('csvs/WGUPS_Addresses.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        # Extracts the address part that is in the third element in each row
        addressData.append(row[2])

# Read distance data from WGUPS_Distances.csv
distanceData = []
with open('csvs/WGUPS_Distance_Table.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        # Convert each value to float
        float_row = [float(value) if value.strip() != '' else '' for value in row]
        distanceData.append(float_row)


# Function to return the distance between two given addresses
def distance_between(address1, address2):
    return distanceData[addressData.index(address1)][addressData.index(address2)]
