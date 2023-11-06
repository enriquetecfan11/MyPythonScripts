# Primero importamos la libreria
import folium 

# Segundo creamos el mapa
mapa = folium.Map(location=[40.4165, -3.7025], zoom_start=12)

# Tercero creamos un marcador y lo añadimos al mapa
folium.Marker(location=[40.4165, -3.7025], popup='Madrid').add_to(mapa)

# Cuarto guardamos el mapa como archivo HTML
mapa.save('mapa.html')
