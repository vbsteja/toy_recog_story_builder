import cv2 
import numpy as np
import tkinter as tk
from tkinter import Label, StringVar
from PIL import Image, ImageTk
import random

from ultralytics import YOLO
def load_model(model_path):
    #load the pretrained YOLO model from ultralytics
    model = YOLO("yolov11n.pt")
    return model

def predict(model, image_path, **params):
    # Load the image
    img = cv2.imread(image_path)
    # ...existing code...

if __name__ == "__main__":
    # Create a window
    window = tk.Tk()
    window.title("Random Image Display")
    window.geometry("800x600")

    # Create a label to display the image
    label = Label(window)
    label.pack()

    # Create a StringVar to hold the image path
    image_path = StringVar()

    # Open webcam once
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        label.config(text="Cannot open webcam")
    else:
        def update_image():
            ret, img = capture.read()
            print("size of the image captured:", img.shape if img is not None else "None")
            if ret and img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img)
                img_pil = img_pil.resize((400, 300), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img_pil)
                label.config(image=img_tk, text="")
                label.image = img_tk  # Keep a reference to avoid garbage collection
            else:
                label.config(text="Failed to read from webcam")
            window.after(30, update_image)  # Schedule next frame

        def on_closing():
            capture.release()
            window.destroy()

        window.protocol("WM_DELETE_WINDOW", on_closing)
        update_image()
    window.mainloop()