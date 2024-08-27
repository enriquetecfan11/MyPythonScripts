import requests

decimals = 4

# Pillar las coordenadas del usuario, el primer valor es la latitud y el segundo la longitud separados por una coma
coords = input("Introduce las coordenadas del punto que quieres visualizar (latitud, longitud): ")

# Separar las coordenadas en dos variables
lat, lon = coords.split(',')
lat = float(lat)
lon = float(lon)

print("Coordenadas del punto seleccionado: ")
print("Latitud: " + str(lat))
print("Longitud: " + str(lon))

# Redondear las coordenadas a 4 decimales
lat = round(lat, decimals)
lon = round(lon, decimals)

margin = 0.01

# Cálculo de los valores de la bbox
xmin = round(lon - margin, decimals)
ymin = round(lat - margin, decimals)
xmax = round(lon + margin, decimals)
ymax = round(lat + margin, decimals)


print("Coordenadas del punto seleccionado: ")
print("Latitud: " + str(lat))
print("Longitud: " + str(lon))
print(" ")

print("Valores de la bbox: ")
print("xmin: " + str(xmin))
print("ymin: " + str(ymin))
print("xmax: " + str(xmax))
print("ymax: " + str(ymax))
print(" ")

bbox = str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax)

imageWith = 400
imageHeight = 400

# Construcción de la URL con los parámetros calculados
# uri = 'http://www.ign.es/wms-inspire/pnoa-ma?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&crs=CRS%3A84&STYLES=&bbox=' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax) + '&layers=OI.OrthoimageCoverage&format=image%2Fpng&width=500&height=500'

uri = 'http://www.ign.es/wms-inspire/pnoa-ma?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&crs=CRS%3A84&STYLES=&bbox=' + bbox + '&layers=OI.OrthoimageCoverage&format=image%2Fpng&width=' + str(imageWith) + '&height=' + str(imageHeight)

# Realizar la solicitud GET para obtener la imagen del mapa
r = requests.get(uri, allow_redirects=True)

filename = 'frame.png'

# Guardar la imagen en un archivo
with open(filename, 'wb') as f:
    f.write(r.content)

print("Mapa generado con éxito. Puedes encontrar la imagen en el archivo:", filename)