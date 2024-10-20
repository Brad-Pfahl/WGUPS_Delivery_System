import csv

distance_file = open('csvs/WGUPS_Distances.csv')
distance_reader = csv.reader(distance_file)
for row in distance_reader:
    print('Hub #' + str(distance_reader.line_num) + ' ' + str(row))
