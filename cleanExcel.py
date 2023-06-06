import pdfplumber
import pandas as pd
from openpyxl import Workbook
import numpy as np
import os

# Importas el archivo excel
excel_file = "tabla_combinada.xlsx"

# Leer el archivo Excel en un DataFrame de pandas
df = pd.read_excel(excel_file)

# Imprimimos el numero de celdas del excel
print("Num celdas del excel: ")
print(df.shape)


# Sustimos los \n por un espacio
df = df.replace('\n', ' ', regex=True)

# Miramos si hay valores nulos y los sustituimos por espacios en blanco
df = df.replace(np.nan, ' ', regex=True)

# Miramos todas las celdas tengan espcaios en blanco y las eliminamos
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Guardamos los cambios
df.to_excel("tabla_combinada_modificada.xlsx", index=False)
print(f"Archivo de Excel '{excel_file}' guardado con éxito.")

