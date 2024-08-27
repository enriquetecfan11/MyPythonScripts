<<<<<<< HEAD
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image
import sys

def initialize_root():
    root = tk.Tk()
    root.title("Displaying Gif")
    root.geometry("1200x800")
    root.resizable(False, False)
    root.configure(bg="black")
    return root

def load_gif(gif_file, frames):
    photoimage_objects = []
    for i in range(frames):
        obj = tk.PhotoImage(file=gif_file, format=f"gif -index {i}")
        photoimage_objects.append(obj)
    return photoimage_objects

def load_all_gifs():
    gifs = {
        "loading": "loading.gif",
        "sad": "sad.gif",
        "happy": "happy.gif",
        "confused": "confused.gif"
    }
    gif_info = {key: Image.open(value) for key, value in gifs.items()}
    gif_frames = {key: info.n_frames for key, info in gif_info.items()}
    gif_images = {key: load_gif(value, gif_frames[key]) for key, value in gifs.items()}
    return gif_images

def switch_gif(gif_images, gif):
    global current_gif
    global current_loop_id
    current_gif = gif
    if current_loop_id:
        root.after_cancel(current_loop_id[0])  # Cancel the current animation loop
    current_loop_id = animate_gif(gif_images[gif], current_loop_id)

def animate_gif(photoimages, loop_id):
    global current_loop_id
    current_loop_id = loop_id
    loop = [None]

    def update_frame(current_frame=0):
        image = photoimages[current_frame]
        gif_label.configure(image=image)
        current_frame = (current_frame + 1) % len(photoimages)
        loop[0] = root.after(50, lambda: update_frame(current_frame))

    update_frame()
    return loop

def create_gif_frame(root):
    gif_frame = tk.Frame(root, bg="black", height=650)
    gif_frame.pack(side="top", fill="both", expand=True)
    gif_label = tk.Label(gif_frame, bg="black", image="")
    gif_label.pack(fill="both", expand=True)
    return gif_frame, gif_label

def create_buttons_frame(root):
    buttons_frame = tk.Frame(root, bg="black", height=150)
    buttons_frame.pack(side="bottom", fill="x")
    return buttons_frame

def create_button_container(buttons_frame):
    canvas = tk.Canvas(buttons_frame, bg="black", height=150)
    canvas.pack(expand=True)
    button_container = tk.Frame(canvas, bg="black")
    button_container.pack(expand=True)
    return button_container

def create_buttons(button_container, gif_images):
    button_style = {"bg": "#4CAF50", "fg": "white", "font": ("Arial", 12), "bd": 0, "activebackground": "#45a049"}

    buttons = {
        "Cargando": lambda: switch_gif(gif_images, "sad"),
        "Habla": lambda: switch_gif(gif_images, "happy"),
        "Escucha": lambda: switch_gif(gif_images, "confused"),
    }

    button_refs = {}

    for i, (text, command) in enumerate(buttons.items()):
        button = tk.Button(button_container, text=text, command=command, **button_style)
        button.grid(row=0, column=i, padx=10, pady=10, ipadx=10, ipady=5)
        button.bind("<Enter>", lambda event: event.widget.config(bg="#388E3C"))
        button.bind("<Leave>", lambda event: event.widget.config(bg="#4CAF50"))
        button_refs[text] = button

    return button_refs

def bind_keys(button_refs):
  root.bind("<Home>", lambda event: button_refs["Cargando"].invoke())
  root.bind("<End>", lambda event: button_refs["Habla"].invoke())
  root.bind("<Prior>", lambda _: button_refs["Escucha"].invoke())

def stop_animation():
  if current_loop_id:
    root.after_cancel(current_loop_id[0])
  root.destroy()

root = initialize_root()
gif_images = load_all_gifs()

gif_frame, gif_label = create_gif_frame(root)
buttons_frame = create_buttons_frame(root)
button_container = create_button_container(buttons_frame)

button_refs = create_buttons(button_container, gif_images)
bind_keys(button_refs)

current_gif = "sad"
current_loop_id = None
switch_gif(gif_images, current_gif)

root.protocol("WM_DELETE_WINDOW", stop_animation)
root.mainloop()
=======
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image
import sys

def initialize_root():
    root = tk.Tk()
    root.title("Displaying Gif")
    root.geometry("1200x800")
    root.resizable(False, False)
    root.configure(bg="black")
    return root

def load_gif(gif_file, frames):
    photoimage_objects = []
    for i in range(frames):
        obj = tk.PhotoImage(file=gif_file, format=f"gif -index {i}")
        photoimage_objects.append(obj)
    return photoimage_objects

def load_all_gifs():
    gifs = {
        "loading": "loading.gif",
        "sad": "sad.gif",
        "happy": "happy.gif",
        "confused": "confused.gif"
    }
    gif_info = {key: Image.open(value) for key, value in gifs.items()}
    gif_frames = {key: info.n_frames for key, info in gif_info.items()}
    gif_images = {key: load_gif(value, gif_frames[key]) for key, value in gifs.items()}
    return gif_images

def switch_gif(gif_images, gif):
    global current_gif
    global current_loop_id
    current_gif = gif
    if current_loop_id:
        root.after_cancel(current_loop_id[0])  # Cancel the current animation loop
    current_loop_id = animate_gif(gif_images[gif], current_loop_id)

def animate_gif(photoimages, loop_id):
    global current_loop_id
    current_loop_id = loop_id
    loop = [None]

    def update_frame(current_frame=0):
        image = photoimages[current_frame]
        gif_label.configure(image=image)
        current_frame = (current_frame + 1) % len(photoimages)
        loop[0] = root.after(50, lambda: update_frame(current_frame))

    update_frame()
    return loop

def create_gif_frame(root):
    gif_frame = tk.Frame(root, bg="black", height=650)
    gif_frame.pack(side="top", fill="both", expand=True)
    gif_label = tk.Label(gif_frame, bg="black", image="")
    gif_label.pack(fill="both", expand=True)
    return gif_frame, gif_label

def create_buttons_frame(root):
    buttons_frame = tk.Frame(root, bg="black", height=150)
    buttons_frame.pack(side="bottom", fill="x")
    return buttons_frame

def create_button_container(buttons_frame):
    canvas = tk.Canvas(buttons_frame, bg="black", height=150)
    canvas.pack(expand=True)
    button_container = tk.Frame(canvas, bg="black")
    button_container.pack(expand=True)
    return button_container

def create_buttons(button_container, gif_images):
    button_style = {"bg": "#4CAF50", "fg": "white", "font": ("Arial", 12), "bd": 0, "activebackground": "#45a049"}

    buttons = {
        "Cargando": lambda: switch_gif(gif_images, "sad"),
        "Habla": lambda: switch_gif(gif_images, "happy"),
        "Escucha": lambda: switch_gif(gif_images, "confused"),
    }

    button_refs = {}

    for i, (text, command) in enumerate(buttons.items()):
        button = tk.Button(button_container, text=text, command=command, **button_style)
        button.grid(row=0, column=i, padx=10, pady=10, ipadx=10, ipady=5)
        button.bind("<Enter>", lambda event: event.widget.config(bg="#388E3C"))
        button.bind("<Leave>", lambda event: event.widget.config(bg="#4CAF50"))
        button_refs[text] = button

    return button_refs

def bind_keys(button_refs):
  root.bind("<Home>", lambda event: button_refs["Cargando"].invoke())
  root.bind("<End>", lambda event: button_refs["Habla"].invoke())
  root.bind("<Prior>", lambda _: button_refs["Escucha"].invoke())

def stop_animation():
  if current_loop_id:
    root.after_cancel(current_loop_id[0])
  root.destroy()

root = initialize_root()
gif_images = load_all_gifs()

gif_frame, gif_label = create_gif_frame(root)
buttons_frame = create_buttons_frame(root)
button_container = create_button_container(buttons_frame)

button_refs = create_buttons(button_container, gif_images)
bind_keys(button_refs)

current_gif = "sad"
current_loop_id = None
switch_gif(gif_images, current_gif)

root.protocol("WM_DELETE_WINDOW", stop_animation)
root.mainloop()
>>>>>>> 23417d7b6ed142e1bebf4f7fa64b340fe4c64c5b
