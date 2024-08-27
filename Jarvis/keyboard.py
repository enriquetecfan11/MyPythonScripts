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
