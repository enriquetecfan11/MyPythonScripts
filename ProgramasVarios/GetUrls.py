import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def obtener_subdirectorios(url):
    # Obtener el contenido de la página web
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        base_url = urlparse(url).scheme + "://" + urlparse(url).netloc
        
        # Encontrar todos los enlaces en la página
        enlaces = soup.find_all("a", href=True)
        subdirectorios = set()

        # Filtrar enlaces que sean subdirectorios de la página base
        for enlace in enlaces:
            enlace_completo = urljoin(base_url, enlace["href"])
            if enlace_completo.startswith(base_url):
                subdirectorios.add(enlace_completo[len(base_url):])

        return subdirectorios
    else:
        print("No se pudo obtener la página:", response.status_code)
        return None

# URL de ejemplo
url_ejemplo = "https://metar-taf.com/?c=244475.127441.4"

# Obtener los subdirectorios y contar la cantidad
subdirectorios = obtener_subdirectorios(url_ejemplo)
if subdirectorios:
    print("Cantidad de subdirectorios:", len(subdirectorios))

# Imprimir los diez primeros subdirectorios
for subdirectorio in list(subdirectorios)[:10]:
    print(subdirectorio)