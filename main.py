import os
import tkinter as tk
from tkinter import filedialog, Label, Button, Frame, messagebox
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageTk

# === Load the model ===
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "fracture_model.keras")
icon_path = os.path.join(script_dir, "trauma.png")

if os.path.exists(model_path):
    model = tf.keras.models.load_model(model_path)
else:
    raise FileNotFoundError(f"❌ Model not found at: {model_path}")

class_names = ["Fractured", "Not Fractured"]

# === Functions ===
def open_image():
    path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.png;*.jpeg")])
    if path:
        result_label.config(text="🔍 Analyzing...", fg="#F8C471")
        root.update_idletasks()
        predict_image(path)

def predict_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    confidence = np.max(prediction) * 100
    predicted_class = class_names[np.argmax(prediction)]

    show_image(image_path)
    result_label.config(
        text=f"🦴 Result: {predicted_class}\n📊 Confidence: {confidence:.2f}%",
        fg="#4CAF50" if predicted_class == "Not Fractured" else "#F44336"
    )

def show_image(image_path):
    img = Image.open(image_path).resize((250, 250))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

def show_team():
    team = "Developed by:\n👨‍💻 Bouagal Houssem Eddine"
    messagebox.showinfo("Development Team", team)

# === UI Setup ===
root = tk.Tk()
root.title("Bone Fracture Detection")
root.geometry("473x626")
root.resizable(False, False)
root.configure(bg="#222831")

# App Icon
if os.path.exists(icon_path):
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)

# === Styles ===
btn_style = {
    "font": ("Segoe UI", 12, "bold"),
    "bg": "#00ADB5",
    "fg": "white",
    "bd": 0,
    "relief": "flat",
    "padx": 10,
    "pady": 6
}
label_style = {
    "font": ("Segoe UI", 14),
    "fg": "#EEEEEE",
    "bg": "#222831"
}

# === Layout ===
main_frame = Frame(root, bg="#222831")
main_frame.pack(pady=20)

# Title
title = tk.Label(main_frame, text="🦴 Bone Fracture Analysis", font=("Segoe UI", 18, "bold"), bg="#222831", fg="white")
title.pack(pady=10)

# Load Button
btn_load = Button(main_frame, text="📂 Load Image", command=open_image, **btn_style)
btn_load.pack(pady=15)

# Image Display
image_label = Label(main_frame, bg="#393E46", width=250, height=250)
image_label.pack(pady=10)

# Prediction Result
result_label = Label(main_frame, text="", **label_style)
result_label.pack(pady=20)

# Footer
footer_frame = Frame(root, bg="#222831")
footer_frame.pack(pady=10)

btn_team = Button(footer_frame, text="👨‍💻 About", font=("Segoe UI", 11), bg="#FFD369", fg="black", command=show_team)
btn_team.pack()

# === Run the App ===
root.mainloop()
