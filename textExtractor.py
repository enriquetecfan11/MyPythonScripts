import requests
from bs4 import BeautifulSoup
import os

urls = [
    "https://www.cursosgis.com/cursos-gvsig/", "https://www.cursosgis.com/cursos-data-science/", "https://www.cursosgis.com/cursos-python/", "https://www.cursosgis.com/curso-desarrollo-gis/"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

counter = 1

for url in urls:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.split("\n") if line.strip()]

        # Generar el nombre del archivo con el contador
        file_name = str(counter) + ".txt"

        with open(file_name, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))

        print("Texto guardado en el archivo:", file_name)

        # Incrementar el contador
        counter += 1
    else:
        print("No se pudo acceder a la página:", url)

