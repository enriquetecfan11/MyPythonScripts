# Itera a través de la lista de elementos de imagen
for img in image_elements:
    # Obtiene la URL de la imagen del atributo 'src'
    img_src = img.get_attribute('src')

    # Intenta abrir la URL de la imagen y descarga la imagen solo si el código de estado es 200
    try:
        if urllib.request.urlopen(img_src).getcode() == 200:
            urllib.request.urlretrieve(img_src, "images/" + str(time.time()) + ".jpg")
            print("Imagen descargada")
        else:
            print("Imagen no descargada - código de estado HTTP no es 200")
    except HTTPError as e:
        print("Imagen no descargada - se produjo una excepción HTTPError: ", e)
