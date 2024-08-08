import tkinter as tk
from PIL import Image, ImageTk

def initialize_window(title):
    root = tk.Tk()
    root.title(title)
    root.geometry("500x700")
    return root

def load_background(root, bg_image_path):
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((500, 700), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
    return bg_label

def create_food_entries(root, food_items):
    entries = []
    for i, (food, calories) in enumerate(food_items):
        canvas = tk.Canvas(root, width=480, height=30, highlightthickness=0)
        canvas.place(x=10, y=30 + i*40)
        food_label = tk.Label(canvas, text=f"{food} : {calories}cal", fg="black", font=("Arial", 10))
        food_label.pack(side=tk.LEFT)
        food_entry = tk.Entry(canvas, fg="black")
        food_entry.pack(side=tk.RIGHT)
        entries.append(food_entry)
    return entries

def calculate_total(entries, food_items, total_label):
    total_calories = 0
    for entry, (food, calories) in zip(entries, food_items):
        try:
            count = int(entry.get())
            total_calories += count * calories
        except ValueError:
            pass
    total_label.config(text=f"Total: {total_calories} cal")

def reset_entries(entries, total_label):
    for entry in entries:
        entry.delete(0, tk.END)
    total_label.config(text="Total: 0 cal")
