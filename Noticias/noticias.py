# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json

# Lista de fuentes con sus URLs reales
fuentes = [
    {
        "nombre": "xataka",
        "URL": "https://www.xataka.com/"
    },
    {
        "nombre": "genbeta",
        "URL": "https://www.genbeta.com/"
    },
    {
        "nombre": "20 Bits",
        "URL": "https://www.20minutos.es/tecnologia/"
    },
    {
        "nombre": "Computer Hoy",
        "URL": "https://computerhoy.com/noticias"
    }
]

def obtenerNoticiasXataka():
    # Obtener la página web
    URL = fuentes[0]["URL"]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtener los titulares y enlaces de las noticias en Xataka
    noticias = soup.find_all("h2", class_="abstract-title")
    noticias_xataka = []

    for noticia in noticias[:2]:  # Tomamos solo las 10 primeras noticias
        titular = noticia.get_text().strip()
        enlace = noticia.find('a')['href']
        noticias_xataka.append({'titular': titular, 'enlace': enlace})

    return noticias_xataka

# Obtener las noticias de Xataka
noticias_xataka = obtenerNoticiasXataka()

# Mostrar los titulares y enlaces
# for i, noticia in enumerate(noticias_xataka, 1):
#     print("--------------------------")
#     print("Xataka")
#     print(f"Noticia {i} - Titular: {noticia['titular']}")
#     print(f"Enlace: {noticia['enlace']}")
#     print("------------------------")

# Obtener las noticias de Genbeta
def obtenerNoticiasGenbeta():
    # Obtener la página web
    URL = fuentes[1]["URL"]  # Usando el índice 1 para Genbeta en la lista de fuentes
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtener los titulares y enlaces de las noticias en Genbeta
    noticias = soup.find_all("h2", class_="abstract-title")
    noticias_genbeta = []

    for noticia in noticias[:2]:  # Tomamos solo las 10 primeras noticias
        titular = noticia.get_text().strip()
        enlace = noticia.find('a')['href']
        noticias_genbeta.append({'titular': titular, 'enlace': enlace})

    return noticias_genbeta

# Obtener las noticias de Genbeta
noticias_genbeta = obtenerNoticiasGenbeta()

# Mostrar los titulares y enlaces de Genbeta
# for i, noticia in enumerate(noticias_genbeta, 1):
#     print("\n")
#     print("--------------------------")
#     print("Genbeta")
#     print(f"Noticia {i} - Titular: {noticia['titular']}")
#     print(f"Enlace: {noticia['enlace']}")
#     print("------------------------")

# Obtener las noticias de 20 Bits
def obtenerNoticias20Bits():
    # Obtener la página web
    URL = fuentes[2]["URL"]  # Usando el índice 2 para 20 Bits en la lista de fuentes
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtener los titulares y enlaces de las noticias en 20 Bits
    noticias = soup.find_all("span", class_="title")
    noticias_20bits = []

    for noticia in noticias[:2]:  # Tomamos solo las 10 primeras noticias
        titular = noticia.get_text().strip()
        enlace = noticia.find('a')['href']
        noticias_20bits.append({'titular': titular, 'enlace': enlace})

    return noticias_20bits

# Obtener las noticias de 20 Bits
noticias_20bits = obtenerNoticias20Bits()

# Mostrar los titulares y enlaces de 20 Bits
# for i, noticia in enumerate(noticias_20bits, 1):
#     print("\n")
#     print("--------------------------")
#     print("20 Bits")
#     print(f"Noticia {i} - Titular: {noticia['titular']}")
#     print(f"Enlace: {noticia['enlace']}")
#     print("------------------------")

# Obtener las noticias de Computer Hoy
def obtenerNoticiasComputerHoy():
    # Obtener la página web
    URL = fuentes[3]["URL"]  # Usando el índice 3 para Computer Hoy en la lista de fuentes
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtener los titulares y enlaces de las noticias en Computer Hoy
    noticias = soup.find_all("h3")
    noticias_computer_hoy = []

    for noticia in noticias[:3]:  # Tomamos solo las 10 primeras noticias
        titular = noticia.get_text().strip()
        enlace = noticia.find('a')['href']
        noticias_computer_hoy.append({'titular': titular, 'enlace': enlace})

    return noticias_computer_hoy

# Obtener las noticias de Computer Hoy
noticias_computer_hoy = obtenerNoticiasComputerHoy()

# Mostrar los titulares y enlaces de Computer Hoy

# for i, noticia in enumerate(noticias_computer_hoy, 1):
#     print("\n")
#     print("--------------------------")
#     print("Computer Hoy")
#     print(f"Noticia {i} - Titular: {noticia['titular']}")
#     print(f"Enlace: {noticia['enlace']}")
#     print("------------------------")

# concatenar todas las noticias en una
noticias = noticias_xataka + noticias_genbeta + noticias_20bits + noticias_computer_hoy

# Mostrar los titulares y enlaces de todas las noticias

# for i, noticia in enumerate(noticias, 1):
#     print("\n")
#     print("--------------------------")
#     print(f"Noticia {i} - Titular: {noticia['titular']}")
#     print(f"Enlace: {noticia['enlace']}")
#     print("------------------------")

# Guardar las noticias en un archivo JSON
with open('noticias.json', 'w', encoding='utf-8') as file:
    json.dump(noticias, file, ensure_ascii=False)

print("Noticias Guardadas Correctamente")