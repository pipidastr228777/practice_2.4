import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import threading

def load_image(url):
    img_data = requests.get(url).content
    img = Image.open(BytesIO(img_data))
    img.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

def get_cat():
    threading.Thread(target=lambda: load_image(requests.get("https://api.thecatapi.com/v1/images/search").json()[0]["url"])).start()

def get_dog():
    threading.Thread(target=lambda: load_image(requests.get("https://dog.ceo/api/breeds/image/random").json()["message"])).start()

root = tk.Tk()
root.title("Коты и собаки")

tk.Button(root, text="Получить кота", command=get_cat).pack()
tk.Button(root, text="Получить собаку", command=get_dog).pack()
label = tk.Label(root)
label.pack()

root.mainloop()