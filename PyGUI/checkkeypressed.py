import keyboard

def on_key_event(event):
    print(f"Key {event.name} {'pressed' if event.event_type == 'down' else 'released'}")

keyboard.hook(on_key_event)

keyboard.wait('esc')  # You can change the key to wait for a different key press
