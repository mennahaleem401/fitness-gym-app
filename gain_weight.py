import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

# Function to initialize the main window
def initialize_window(title):
    root = tk.Tk()
    root.title(title)
    root.geometry("400x600")
    return root

# Function to load and display the background image
def load_background(root, bg_image_path):
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((400, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
    return bg_label

# Function to go back to the diet plan
def go_back_to_diet_plan():
    subprocess.Popen(['python', 'diet_plan_page.py'])
    root.destroy()

# Function to open Gain_weight window
def Gain_weight():
    global root
    root = initialize_window("Gain Weight Tips")
    load_background(root, r"Assets\WhatsApp Image 2024-07-31 at 10.55.46_5b40fdba.jpg")

    custom_font = ("Comic Sans MS", 14, "italic")
    basic = tk.Label(root, text="DEAR FAT PREPARE TO DIE", font=custom_font, fg="gray", bg="#000")
    basic.grid(row=0, column=0, columnspan=4, sticky='we', padx=50, pady=30)

    # Weight gain tips
    tips = [
        "●   Have high-calorie drinks",
        "●   Add extra calories to your meals",
        "●   Have snacks that are easy to prepare",
        "●   Add carb to your meals",
        "●   Add to food 300 to 500 extra calories a day",
        "●   Do not fill up on drinks before eating meals",
        "●   Do not rely on chocolate sugary drinks to gain weight",
        "●   Get enough sleep",
        "●   Add more protein to your food",
        "●   Get more fiber",
        "●   Should eat salad",
        "●   Keep a food and weight diary",
        "●   Eat varied, colorful, nutritionally dense foods",
        "●   Engage in regular physical activity and exercise",
        "●   Reduce your plate size",
        "●   Get enough sleep"
    ]

    for i, tip in enumerate(tips, start=1):
        tk.Label(root, text=tip, font="Helvetica 10 bold", fg="gray", bg="#000").grid(row=i, column=0, sticky='w', pady=15, padx=20)

    # Back button
    back_btn = ttk.Button(root, text="<<<", command=go_back_to_diet_plan)
    back_btn.place(x=30, width=50, y=525)

    root.mainloop()

if __name__ == "__main__":
    Gain_weight()
