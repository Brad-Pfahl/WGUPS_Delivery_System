from src.dijkstra import Graph, Vertex, dijkstra_shortest_path, get_shortest_path, address_list, g
from src.distance import get_distances, distance_between
from src.packages import package_table
from src.trucks import truck_0, truck_1, truck_2
'''
# Build the graph using the addresses of the packages
def build_graph_for_truck(truck):
    g = Graph()  # Initialize a new graph
    address_list = [package_table.search(pkg_id).pkg_address for pkg_id in
                    truck.pkg_list]  # Get addresses from packages

    print("Adding vertices to the graph:")
    for address in address_list:
        print(f"Adding vertex: {address}")
        g.add_vertex(Vertex(address))

    for i in range(len(address_list)):
        for j in range(len(address_list)):
            if i != j:  # Avoid adding an edge to itself
                print(f"Calculating distance between: {address_list[i]} and {address_list[j]}")
                weight = distance_between(address_list[i], address_list[j])
                print(f"Adding edge from {address_list[i]} to {address_list[j]} with weight {weight}")
                g.add_undirected_edge(Vertex(address_list[i]), Vertex(address_list[j]), weight)

    print("Adding edges to the graph:")
    for i in range(len(address_list)):
        for j in range(len(address_list)):
            if i != j:  # Avoid adding an edge to itself
                # Pass the address strings instead of Vertex objects
                weight = distance_between(address_list[i], address_list[j])
                print(f"Adding edge from {address_list[i]} to {address_list[j]} with weight {weight}")
                g.add_undirected_edge(Vertex(address_list[i]), Vertex(address_list[j]), weight)

    return g


def run_dijkstra_for_trucks():
    for truck in [truck_0, truck_1, truck_2]:
        print(f"Calculating shortest paths for Truck {truck.truck_id}...")
        graph = build_graph_for_truck(truck)
        # Implement Dijkstra's algorithm here for the graph



# Run the algorithm for all trucks
run_dijkstra_for_trucks()
print(run_dijkstra_for_trucks())
'''
