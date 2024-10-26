# Dijkstra.py
# Dijkstra shortest path - START
from src.distance import addressData, distanceData, distance_between
from src.packages import package_table
from src.trucks import truck_0, truck_1, truck_2, Truck


# Modified version of Dijkstra Algorithm using 'WGU C950 Webinar-3 How to Dijkstra' as a starting point
class Vertex:
    # Constructor for a new Vertx object. All vertex objects
    # start with a distance of positive infinity.
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None


class Graph:
    def __init__(self):
        self.adjacency_list = {}  # vertex dictionary {key:value}
        self.edge_weights = {}  # edge dictionary {key:value}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []  # {vertex_1: [], vertex_2: [], ...}

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        # {(vertex_1,vertex_2): 484, (vertex_1,vertex_3): 626, (vertex_2,vertex_6): 1306, ...}
        self.adjacency_list[from_vertex].append(to_vertex)
        # {vertex_1: [vertex_2, vertex_3], vertex_2: [vertex_6], ...}

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


# Dijkstra shortest path
def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []

    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)
        # unvisited_queue = [vertex_1, vertex_2, ...]

    # Start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            # print(unvisited_queue[i].label, unvisited_queue[i].distance, unvisited_queue[i].pred_vertex)
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        # print("From Start Vertex to current_vertex.label: " + current_vertex.label +" distance: " + str(
        # current_vertex.distance))

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:  # values from  dictionary
            # if current_vertex = vertex_1 => adj_vertex in [vertex_2, vertex_3], if vertex_2 => adj_vertex in [
            # vertex_6], ...
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]  # values from dictionary
            # edge_weight = 484 then 626 then 1306, ...}
            alternative_path_distance = current_vertex.distance + edge_weight

            # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path

'''
def get_shortest_path_city(start_vertex, end_vertex, myHash):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        myMovie = myHash.search(int(current_vertex.label))
        path = " -> " + myMovie.city + path
        current_vertex = current_vertex.pred_vertex
    path = "Salt Lake City " + path
    return path
'''

# ---------------------------------------------------------


def dijkstraAlgorithmShortestPath(truck):
    # Dijkstra shortest path main 
    # Program to find shortest paths from vertex A.
    g = Graph()
    vertices = {}

    # Create a vertex for the hub and add it to the graph
    hub_address = "4001 South 700 East"
    hub_vertex = Vertex(hub_address)
    g.add_vertex(hub_vertex)
    vertices[hub_address] = hub_vertex

    # Load package data and add vertices
    for pkg_id in truck.pkg_list:
        package = package_table.search(pkg_id)
        if not package:
            print(f"Package with ID {pkg_id} not found")
            continue

        address = package.pkg_address

        # Create a new vertex for each unique address.
        if address not in vertices:
            new_vertex = Vertex(address)
            g.add_vertex(new_vertex)
            vertices[address] = new_vertex

            # Add a directed edge from the hub to this package address
            weight = distance_between(hub_address, address)  # Calculate distance from hub to package
            g.add_directed_edge(hub_vertex, new_vertex, weight)  # Add edge from hub to package

    # Load distance data and add edges between vertices.
    for address1 in vertices:
        for address2 in vertices:
            if address1 != address2:
                # Use the distance_between function to get the distance.
                weight = distance_between(address1, address2)
                g.add_directed_edge(vertices[address1], vertices[address2], weight)

    # Pick the hub as the start vertex
    start_vertex = hub_vertex
    dijkstra_shortest_path(g, start_vertex)

    # Display shortest path to each vertex
    truck_mileage = 0
    print("\nDijkstra shortest path:")
    for v in g.adjacency_list:
        if v.pred_vertex is None and v is not start_vertex:
            print(f"{start_vertex.label} to {v.label} ==> no path exists")
        else:
            path = get_shortest_path(start_vertex, v)
            print(f"{start_vertex.label} to {v.label} ==> {path} (total distance: {v.distance})")
            truck_mileage += v.distance  # Add the distance to the total mileage of our truck

    truck.truck_mileage = truck_mileage


'''
dijkstraAlgorithmShorthestPath()
# Dijkstra shortest path - END

# main - START
if __name__ == '__main__':
    print("\nWelcome to C950: Classic Movies: Hash Table, CSV Import, Greedy Algorithm, Dijkstra Algorithm")

    # loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Get Movie Data")
        print("2. Run Greedy Algorithm with a Budget")
        print("3. Run Dijkstra Algorithm")
        print("4. Exit the Program")
        option = input("Chose an option (1,2,3 or 4): ")
        if option == "1":
            getMovieData()
        elif option == "2":
            budget = int(input("What is your budget (ex. 150)? "))
            greedyAlgorithmMinExpenses(budget)
        elif option == "3":
            dijkstraAlgorithmShorthestPath()
        elif option == "4":
            isExit = False
        else:
            print("Wrong option, please try again!")          
# main - END
'''
