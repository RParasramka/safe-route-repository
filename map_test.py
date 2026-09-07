import folium

# Center the map on Loughborough
m = folium.Map(location=[52.7666, -1.2039], zoom_start=13)

# Your three test points from earlier, with their elevations
points = [
    {"lat": 52.7666, "lng": -1.2039, "elevation": 47.0, "label": "Start point"},
    {"lat": 52.7700, "lng": -1.2100, "elevation": 50.0, "label": "Highest point"},
    {"lat": 52.7600, "lng": -1.1900, "elevation": 45.0, "label": "Lower point"},
]

for p in points:
    folium.Marker(
        location=[p["lat"], p["lng"]],
        popup=f"{p['label']}: {p['elevation']}m",
        icon=folium.Icon(color="green" if p["elevation"] >= 48 else "red")
    ).add_to(m)

m.save("map.html")
print("Map saved — open map.html in your browser")