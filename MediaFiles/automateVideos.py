import os
import csv

# Ruta del directorio que contiene los archivos .mp4
mp4_directory = r''

# Ruta donde van los csv
csv_directory = r''

# Función para crear y escribir en un archivo CSV
def create_csv(file_path):
    csv_path = os.path.join(csv_directory, os.path.splitext(os.path.basename(file_path))[0] + '.csv')
    
    with open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['type', 'number', 'begins', 'ends'])
    
    return csv_path

# Iterar a través de los archivos .mp4 en el directorio
for filename in os.listdir(mp4_directory):
    if filename.endswith('.MP4'):
        mp4_path = os.path.join(mp4_directory, filename)
        csv_path = create_csv(mp4_path)
        print(f'Creado archivo CSV: {csv_path}')

print("Proceso completado.")
