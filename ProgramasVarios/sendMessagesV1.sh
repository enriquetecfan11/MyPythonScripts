#!/bin/bash

# Definir variables
ID_BOT="1984896147:AAHPlXoRiVSqN8oWkieMz4GeFYfZzFUVxOw"
ID_GRUPO="-4125664054"

# Función para enviar un mensaje
enviar_mensaje() {
    mensaje="$1"
    curl -s -X POST "https://api.telegram.org/bot$ID_BOT/sendMessage" \
        -d "chat_id=$ID_GRUPO" \
        -d "text=$mensaje" \
        -d "parse_mode=HTML" >/dev/null
    echo "Mensaje enviado: $mensaje"
}

# Función para obtener el precio de Bitcoin
get_bitcoin_price() {
    precio=$(curl -s "https://api.coindesk.com/v1/bpi/currentprice.json" | jq -r ".bpi.USD.rate")
    echo "El precio del Bitcoin es: $precio"
    enviar_mensaje "El precio del Bitcoin es: $precio"
}


# Ejecutar las funciones
get_bitcoin_price

