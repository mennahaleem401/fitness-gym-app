import tkinter as tk
from PIL import Image, ImageTk
import os
import sqlite3
import sys
from globalvariables import AppController
import subprocess

conn=sqlite3.connect("GYMbd1.db")

if len(sys.argv) < 2:
    print("Usage: python lunchCalories.py <ssn>")
    sys.exit(1)

ssn = sys.argv[1]
# Initialize the AppController and set the ssn
controller = AppController()
controller.set_data("ssn", ssn)
print(ssn)
def insert_data(result):
 try:
    cursor = conn.cursor()
    cursor.execute("UPDATE calories set dinner_cal=?WHERE visitor_id=?", (result, ssn))
    conn.commit()
 except Exception as e:
     print(e)
# Function to initialize the main window
def initialize_window(title):
    root = tk.Tk()
    root.title(title)
    root.geometry("500x700")
    return root

# Function to load and display the background image
def load_background(root, bg_image_path):
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((500, 700), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
    return bg_label

# Function to create labels and entries for food items
def create_food_entries(root, food_items):
    entries = []
    for i, (food, calories) in enumerate(food_items):
        food_label = tk.Label(root, text=f"{food} : {calories} cal", fg="white", font=("Comic Sans MS", 10), bg="black")
        food_label.place(x=10, y=30 + i * 40)
        food_entry = tk.Entry(root, fg="black", width=5)
        food_entry.place(x=400, y=30 + i * 40)
        entries.append(food_entry)
    return entries

# Function to calculate total calories
def calculate_total(entries, food_items, total_label,id_entry):
    total_calories = 0
    for entry, (food, calories) in zip(entries, food_items):
        try:
            count = int(entry.get())
            total_calories += count * calories
        except ValueError:
            pass
    total_label.config(text=f"Total: {total_calories} cal")
    insert_data(total_calories)

# Function to reset all entries and the total label
def reset_entries(entries, total_label,id_entry):
    for entry in entries:
        entry.delete(0, tk.END)
    total_label.config(text="Total: 0 cal")

# Function to switch to the system.py
def open_system_window(current_root):
    current_root.destroy()
    subprocess.run(['python', 'system.py', ssn])  # Ensure system.py is in the same directory or provide the correct path

# Main function for the calorie counter window
def third_window():
    food_items = [
        ("Tea with Milk & Sugar (1.0 cup)", 73),
        ("Coffee with Milk & Sugar (1.0 cup)", 135),
        ("Skimmed Milk (1.0 glass)", 167),
        ("Apple (1.0 large)", 131),
        ("Orange (1.0 fruit)", 62),
        ("Marie Gold, Britannia (4.0 piece)", 89),
        ("Banana, Ripe (1.0 small)", 117),
        ("Samosa (1.0 piece)", 349),
        ("Peanuts, Roasted (100.0 grams)", 340)
    ]

    bg_image_path = r"Assets\WhatsApp Image 2024-07-31 at 10.55.46_5b40fdba.jpg"  # Path to the uploaded background image

    root = initialize_window("Calorie Counter")
    load_background(root, bg_image_path)

    entries = create_food_entries(root, food_items)
    '''id_label = tk.Label(root, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
    id_label.place(x=350, y=400)
    id_entry = tk.Entry(root, font=("Arial", 15), fg="#000", bg="#fff", width=10, highlightcolor='gray',
                        highlightthickness=5, highlightbackground='gray')
    id_entry.place(x=350, y=450)'''

    total_label = tk.Label(root, text="Total: 0 cal", fg="white", font=("Comic Sans MS", 14), bg="black")
    total_label.place(x=200, y=600)

    total_button = tk.Button(root, text="Total", command=lambda: calculate_total(entries, food_items, total_label,ssn), bg="gray", fg="black", font=("Comic Sans MS", 12))
    total_button.place(x=200, y=550)

    reset_button = tk.Button(root, text="Reset", command=lambda: reset_entries(entries, total_label,ssn), bg="gray", fg="black", font=("Comic Sans MS", 12))
    reset_button.place(x=200, y=650)

    left_button = tk.Button(root, text="<<<", command=lambda: open_system_window(root), bg="black", fg="white", font=("Comic Sans MS", 20, "bold"), bd=0)
    left_button.place(x=20, y=640)

    '''right_button = tk.Button(root, text=">>>", command=lambda: open_third_window(root), bg="black", fg="white", font=("Comic Sans MS", 20, "bold"), bd=0)
    right_button.place(x=430, y=640)'''

    root.mainloop()

if __name__ == "__main__":
    third_window()
