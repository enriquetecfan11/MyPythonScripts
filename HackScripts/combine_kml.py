import csv
import simplekml

def kml_to_csv(kml_file, csv_file):
    # Leer el archivo KML
    kml = simplekml.Kml()
    kml.load(kml_file)
    
    # Crear un archivo CSV
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Escribir las cabeceras en el archivo CSV
        writer.writerow(['Name', 'Description', 'Latitude', 'Longitude'])
        
        # Iterar sobre cada lugar en el archivo KML y escribirlo en el archivo CSV
        for placemark in kml.features():
            if hasattr(placemark, 'geometry'):
                name = placemark.name
                description = placemark.description
                coords = placemark.geometry.coords
                latitude = coords[0][1]
                longitude = coords[0][0]
                
                writer.writerow([name, description, latitude, longitude])

# Ruta del archivo KML de entrada y archivo CSV de salida
kml_file = 'input.kml'
csv_file = 'output.csv'

# Convertir el archivo KML a CSV
kml_to_csv(kml_file, csv_file)
