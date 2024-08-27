#!/usr/bin/env python3
import requests
import datetime

idBot = '1984896147:AAHPlXoRiVSqN8oWkieMz4GeFYfZzFUVxOw'
idGrupo = '-4125664054'


def enviarMensaje(mensaje):   
    requests.post('https://api.telegram.org/bot' + idBot + '/sendMessage',
              data={'chat_id': idGrupo, 'text': mensaje, 'parse_mode': 'HTML'})
    print('Mensaje enviado')

def getBitcoinPrice():
    # https://api.coindesk.com/v1/bpi/currentprice.json
    respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    precio = respuesta.json()['bpi']['USD']['rate']
    print('El precio del Bitcoin es: ' + precio)
    enviarMensaje('El precio del Bitcoin es: ' + precio)


def enviarDocumento(ruta):
    requests.post('https://api.telegram.org/bot' + idBot + '/sendDocument',
              files={'document': (ruta, open(ruta, 'rb'))},
              data={'chat_id': idGrupo, 'caption': 'imagen caption'})
    
def getBot():
    respuesta = requests.get('https://api.telegram.org/bot' + idBot + '/getMe')
    print(respuesta.json())


# mensaje = 'Hola Mundo son las ' + str(datetime.datetime.now())
mensaje_comando = "/tiempo Mondejar"

#enviarMensaje(mensaje_comando)
# getBot()

getBitcoinPrice()

# https://api.telegram.org/bot1984896147:AAHPlXoRiVSqN8oWkieMz4GeFYfZzFUVxOw/getMe