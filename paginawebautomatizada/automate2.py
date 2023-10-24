import pandas as pd

# Cargar los datos desde el CSV donde tenemos los datos de los productos
df_productos = pd.read_csv('nichobaterias2-productos.csv', delimiter=';', encoding='utf-8')

# Datos del sitio
site_data = df_productos.iloc[0]

# Crear una variable para almacenar el HTML de los productos
product_section_html = ""

# Recorrer los productos del excel
for index, row in df_productos.iloc[1:].iterrows():
    product_html = f"""
        <div class="product">
            <img src="{row['product.image']}" alt="{row['product.name']}">
            <h3>{row['product.name']}</h3>
            <p>{row['product.description']}</p>
            <a href="" class="affiliate-link">{row['product.link']}</a>
        </div>
    """

    # Agregar el HTML del producto a la sección de productos
    product_section_html += product_html

# CSV de la información de la página
df_page_info = pd.read_csv('nichobaterias2.csv', delimiter=';', encoding='utf-8')

# Recorrer las primeras filas del csv
for index, row in df_page_info.iloc[:1].iterrows():
  # Imprimir el row
  # print(row)
  # Crear el hmtl con los datos de la fila
  html = f"""<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <title>{row['site.title']}</title>
    </head>
    <body>
        <header>
            <h1>{row['site.title']}</h1>
            <p>{row['site.domain']}</p>
        </header>
        <main>
            <section class="product-section">
                <h2>{row['product.header.category']}</h2>
                <p>{row['product.suheader.category']}</p>
                <div class="product-column">
                    {product_section_html}
                </div>
            </section>
        </main>
        <footer>
            <p>&copy; {row['site.title']}</p>
        </footer>
    </body>
    </html>"""
  
  # print(html)

# Guardar el HTML en un archivo o hacer lo que necesites con él
with open(f'output{index}.html', 'w') as file:
    file.write(html)
    print(f"Archivo {index} guardado")
