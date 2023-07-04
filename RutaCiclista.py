# -*- coding: utf-8 -*-

import folium
import osmnx as ox
import matplotlib.pyplot as plt
import requests


def obtener_altitud(latitud, longitud):
    url = "https://api.open-elevation.com/api/v1/lookup?locations=" + str(latitud) + "," + str(longitud)
    respuesta = requests.get(url)
    datos = respuesta.json()
    if datos["results"]:
        return datos["results"][0]["elevation"]
    else:
        return None

def obtener_ruta(lat_origen, lon_origen, lat_destino, lon_destino):
    # Use the `graph_from_point` function to retrieve the street network graph
    graph = ox.graph_from_point((lat_origen, lon_origen), network_type='all')
    
    # Use the `distance.nearest_nodes` function to get the nearest nodes to the origin and destination points
    origen_node = ox.distance.nearest_nodes(graph, lon_origen, lat_origen)
    destino_node = ox.distance.nearest_nodes(graph, lon_destino, lat_destino)
    
    # Use the `shortest_path` function to obtain the shortest path between the origin and destination nodes
    ruta = ox.shortest_path(graph, origen_node, destino_node, weight='length')
    
    # Create a map object
    mapa = folium.Map(location=[lat_origen, lon_origen], zoom_start=12)
    
    # Draw the route on the map
    folium.PolyLine(locations=[(graph.nodes[n]['y'], graph.nodes[n]['x']) for n in ruta], color='blue').add_to(mapa)
    
    # Calculate the altitude for the points along the route
    altitudes = []
    for node in ruta:
        latitud = graph.nodes[node]['y']
        longitud = graph.nodes[node]['x']
        altitud = obtener_altitud(latitud, longitud)
        altitudes.append(altitud)
    
    # Create an altitude plot
    etiquetas = [f"Punto {i}" for i in range(len(altitudes))]
    
    plt.plot(etiquetas, altitudes)
    plt.xlabel("Puntos de Ruta")
    plt.ylabel("Altitud (metros)")
    plt.title("Altimetría de la Ruta")
    plt.grid(True)
    
    # Save the altitude plot as an image
    plt.savefig("ruta/altimetria.png")
    
    # Save the map as an HTML file
    mapa.save("ruta/mapa_interactivo.html")
    
    # Return the altitudes
    return altitudes

latitud_origen, longitud_origen = input("Introduce la latitud y longitud del punto de origen separadas por una coma: ").split(",")
latitud_destino, longitud_destino = input("Introduce la latitud y longitud del punto de destino separadas por una coma: ").split(",")

latitud_origen = float(latitud_origen.strip())
longitud_origen = float(longitud_origen.strip())
latitud_destino = float(latitud_destino.strip())
longitud_destino = float(longitud_destino.strip())

obtener_ruta(latitud_origen, longitud_origen, latitud_destino, longitud_destino)

print("Mapa interactivo guardado")
