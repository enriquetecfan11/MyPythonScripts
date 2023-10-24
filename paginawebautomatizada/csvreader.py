import pandas as pd

# Cargar los datos desde el CSV donde tenemos los datos de los productos
df_productos = pd.read_csv('nichobaterias2-productos.csv', delimiter=',')

# Datos del sitio
site_data = df_productos.iloc[0]

# Crear una variable para almacenar el HTML de los productos
product_section_html = ""

# Recorrer los productos a partir de la segunda fila (índice 1)
for index, row in df_productos.iloc[1:].iterrows():
  print(row)

  # Desde el row trae el product.name
  print(row['product.name'])