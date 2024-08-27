import requests

# Coordenadas (41.596487480603805, -3.071592537907651)
lat = 41.59628538281357
lon = -3.0656874803815777


# Cálculo de los valores de la bbox
xmin = lon - 0.01
ymin = lat - 0.01
xmax = lon + 0.01
ymax = lat + 0.01

# Construcción de la URL con los parámetros calculados
uri = 'http://www.ign.es/wms-inspire/pnoa-ma?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&crs=CRS%3A84&STYLES=&bbox=' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax) + '&layers=OI.OrthoimageCoverage&format=image%2Fpng&width=500&height=500'

# Realizar la solicitud GET para obtener la imagen del mapa
r = requests.get(uri, allow_redirects=True)

# Guardar la imagen en un archivo
with open('frame.png', 'wb') as f:
    f.write(r.content)

print("Mapa generado con éxito. Puedes encontrar la imagen en el archivo 'mapa.png'")