import osmnx as ox
import networkx as nx

# Loughborough town centre coordinates, with a 5km radius around it
center_point = (52.7666, -1.2039)
G = ox.graph_from_point(center_point, dist=5000, network_type="walk")

print(f"Graph has {len(G.nodes)} nodes and {len(G.edges)} edges")

# Find the nearest graph node to a start and end coordinate
start_point = (52.7666, -1.2039)  # Loughborough town centre
end_point = (52.7700, -1.2100)    # your earlier "highest point" test coordinate

start_node = ox.nearest_nodes(G, start_point[1], start_point[0])  # note: (lng, lat) order here
end_node = ox.nearest_nodes(G, end_point[1], end_point[0])

# Calculate the shortest path by distance
route = nx.shortest_path(G, start_node, end_node, weight="length")

# Calculate the total distance of that route in meters
route_length = nx.shortest_path_length(G, start_node, end_node, weight="length")

print(f"Route has {len(route)} nodes")
print(f"Total distance: {route_length:.0f} meters")
walking_speed_kmh = 5  # average walking pace
route_length_km = route_length / 1000
estimated_time_minutes = (route_length_km / walking_speed_kmh) * 60

print(f"Estimated walking time: {estimated_time_minutes:.1f} minutes")
route_edges = ox.routing.route_to_gdf(G, route)
route_map = route_edges.explore(color="red", tiles="OpenStreetMap")
route_map.save("route_map.html")
print("Route map saved — open route_map.html in your browser")
