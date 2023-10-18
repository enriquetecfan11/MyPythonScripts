import pandas as pd

# Cargar los datos desde el CSV
df = pd.read_csv('nichobaterias.csv', delimiter=',')

# Recorrer cada fila del DataFrame
for index, row in df.iterrows():
  print(row)

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
                    <div class="product">
                        <img src="{row['product.image']}" alt="Cargador USB-C">
                        <h3>{row['product.name']}</h3>
                        <p>{row['product.description']}</p>
                        <a href="{row['product.link']}" class="affiliate-link">{row['product.link']}</a>
                    </div>
                </div>
            </section>
        </main>
        <footer>
            <p>&copy; {row['site.title']}</p>
        </footer>
    </body>
    </html>"""
  
  print(html)

# Guardar el HTML en un archivo o hacer lo que necesites con él
with open(f'output{index}.html', 'w') as file:
    file.write(html)
