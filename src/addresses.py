import csv

address_file = open('csvs/WGUPS_Addresses.csv')
address_reader = csv.reader(address_file)
for row in address_reader:
    print(row)