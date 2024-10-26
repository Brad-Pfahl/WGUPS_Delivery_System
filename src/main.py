# Author: Brad Pfahl
# Student ID: 011070820
# Title: C950 WGUPS Routing Program
from src.dijkstra import dijkstraAlgorithmShortestPath
from src.packages import *
from src.trucks import truck_0
from src.distance import *
from src.trucks import *

dijkstraAlgorithmShortestPath(truck_0)
dijkstraAlgorithmShortestPath(truck_1)
dijkstraAlgorithmShortestPath(truck_2)

total_mileage = int(truck_0.truck_mileage + truck_1.truck_mileage + truck_2.truck_mileage)
print(total_mileage)