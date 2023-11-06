import socketio

# Configura el cliente Socket.IO
sio = socketio.Client()

# Define la función para manejar el evento 'connect'
@sio.on('connect')
def on_connect():
    print('Conectado al servidor WebSocket')

# Define la función para manejar el evento 'chat message'
@sio.on('chat message')
def on_chat_message(msg):
    print('msg -> ', msg)

# Conéctate al servidor WebSocket
sio.connect('http://localhost:3000')  # Cambia esto con la dirección de tu servidor

# Espera a que se presione Ctrl+C para desconectarse
try:
    while True:
        pass

except KeyboardInterrupt:
    sio.disconnect()  # Desconéctate cuando se presiona Ctrl+C
