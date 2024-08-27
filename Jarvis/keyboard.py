<<<<<<< HEAD
from pynput import keyboard

def on_press(key):
    try:
        print('Letra presionada: {0}'.format(key.char))
    except AttributeError:
        print('Tecla especial presionada: {0}'.format(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Mantén el programa en ejecución hasta que el usuario lo detenga
input()
listener.stop()
=======
from pynput import keyboard

def on_press(key):
    try:
        print('Letra presionada: {0}'.format(key.char))
    except AttributeError:
        print('Tecla especial presionada: {0}'.format(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Mantén el programa en ejecución hasta que el usuario lo detenga
input()
listener.stop()
>>>>>>> 23417d7b6ed142e1bebf4f7fa64b340fe4c64c5b
