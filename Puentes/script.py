import folium
import pandas as pd
from folium.plugins import MarkerCluster
from geopy.distance import geodesic

# Punto de referencia
referencia = (40.0, -3.0)

# Cargar el archivo GeoJSON
data = pd.read_json('puentes.geojson')

# Crear un mapa centrado en España
mapa = folium.Map(location=[40.4637, -3.7492], zoom_start=6)

# Crear un objeto MarkerCluster
marker_cluster = MarkerCluster()

# Lista para almacenar las distancias de los puntos al punto de referencia
distancias = []

# Iterar sobre cada punto en el GeoJSON
for feature in data['features']:
    # Obtener las propiedades y coordenadas del punto
    properties = feature['properties']
    coordinates = feature['geometry']['coordinates']
    
    # Calcular la distancia entre el punto y el punto de referencia
    distancia = geodesic(referencia, (coordinates[1], coordinates[0])).kilometers
    
    # Agregar la distancia a la lista de distancias
    distancias.append(distancia)
    
# Obtener los N puntos más cercanos al punto de referencia
n = 100  # Número de puntos a mostrar
indices_cercanos = sorted(range(len(distancias)), key=lambda i: distancias[i])[:n]

# Iterar sobre los puntos cercanos y crear marcadores
for index in indices_cercanos:
    feature = data['features'][index]
    properties = feature['properties']
    coordinates = feature['geometry']['coordinates']
    
    # Obtener los valores de las columnas
    id = properties['ID']
    comunidad = properties['COMUNIDAD']
    provincia = properties['PROVINCIA']
    url = properties['url']
    codigo = properties['CÓDIGO']
    
    # Crear un marcador para el punto
    marker = folium.Marker([coordinates[1], coordinates[0]], popup=f'ID: {id}<br>'
                                                              f'Código Puente: {codigo}<br>'
                                                              f'Comunidad: {comunidad}<br>'
                                                              f'Provincia: {provincia}<br>'
                                                              f'<a href="{url}" target="_blank">Ver en Google Maps Street View</a>')
    
    # Agregar el marcador al objeto MarkerCluster
    marker_cluster.add_child(marker)

# Agregar el objeto MarkerCluster al mapa
mapa.add_child(marker_cluster)

# Añadir capa de OpenStreetMap al mapa
folium.TileLayer('openstreetmap').add_to(mapa)

# Añadir capa de Google Hybrid al mapa
google_hybrid = folium.TileLayer(tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',attr='Google Hybrid', name='Google Hybrid', overlay=True)
google_hybrid.add_to(mapa)

# Agregar capas al control de capas
folium.LayerControl().add_to(mapa)

# Guardar el mapa interactivo en formato HTML
mapa.save('InspecionDeViaductos.html')
