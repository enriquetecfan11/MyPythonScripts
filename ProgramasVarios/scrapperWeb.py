import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv

# Función para extraer todas las URLs de una página web junto con el código de estado
def get_all_urls(page_url, base_url):
    try:
        response = requests.get(page_url)
        status_code = response.status_code
        if status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            urls = {}
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(base_url, href)
                    if urlparse(full_url).netloc == urlparse(base_url).netloc:
                        name = link.text.strip() or full_url
                        urls[full_url] = (name, status_code)
            return urls
        else:
            print(f"Error al acceder a la página: {status_code}")
            return {page_url: ("Error", status_code)}
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return {page_url: ("Error", None)}

# Función para realizar el crawling de todas las subpáginas con un límite de URLs
def crawl_website(start_url, max_depth=2, max_urls=50):
    visited_urls = set()
    urls_to_visit = [(start_url, 0)]
    all_urls = {}

    while urls_to_visit and len(all_urls) < max_urls:
        current_url, depth = urls_to_visit.pop(0)
        if current_url not in visited_urls and depth <= max_depth:
            print(f"Crawling: {current_url} (Depth: {depth})")
            visited_urls.add(current_url)
            urls = get_all_urls(current_url, start_url)
            for url, (name, status_code) in urls.items():
                if len(all_urls) >= max_urls:
                    break
                all_urls[url] = (name, status_code)
            urls_to_visit.extend([(url, depth + 1) for url in urls if len(all_urls) < max_urls])

    return all_urls

# Función para exportar URLs a un archivo CSV, incluyendo el código de estado
def export_urls(all_urls):
    with open('urls.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre', 'URL', 'Código de Estado'])
        for url, (name, status_code) in all_urls.items():
            writer.writerow([name, url, status_code])

# Ejemplo de uso
start_url = 'https://www.luisllamas.es/tutoriales-arduino/'
max_urls = 10000  # Número máximo de URLs que deseas extraer
all_urls = crawl_website(start_url, max_depth=2, max_urls=max_urls)

export_urls(all_urls)
print(f"Se han exportado {len(all_urls)} URLs al archivo urls.csv")
