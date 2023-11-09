import sounddevice as sd

def print_input_devices():
    input_devices = sd.query_devices()
    print("Dispositivos de entrada de audio:")
    for device in input_devices:
        if device['max_input_channels'] > 0:
            print(f"Nombre: {device['name']}")
            print(f"Índice: {device['index']}")
            print()

if __name__ == "__main__":
    print_input_devices()
