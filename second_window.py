import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import sys
from globalvariables import AppController
import subprocess

# Check if the argument is provided
if len(sys.argv) < 2:
    print("Usage: python eveningSnacks.py <ssn>")
    sys.exit(1)

ssn = sys.argv[1]

# Initialize the AppController and set the ssn
controller = AppController()
controller.set_data("ssn", ssn)

conn = sqlite3.connect("GYMbd1.db")


def insert_data(result, id_entry):
    ssn = controller.get_data("ssn")
    cursor = conn.cursor()
    cursor.execute("UPDATE calories set eveningSnackes_cal=? WHERE visitor_id=?", (result, ssn))
    conn.commit()

print(ssn)
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
        canvas = tk.Canvas(root, width=480, height=30, highlightthickness=0)
        canvas.place(x=10, y=30 + i * 40)
        food_label = tk.Label(canvas, text=f"{food} : {calories}cal", fg="black", font=("Arial", 10))
        food_label.pack(side=tk.LEFT)
        food_entry = tk.Entry(canvas, fg="black")
        food_entry.pack(side=tk.RIGHT)
        entries.append(food_entry)
    return entries


# Function to calculate total calories
def calculate_total(entries, food_items, total_label, id_entry):
    total_calories = 0
    for entry, (food, calories) in zip(entries, food_items):
        try:
            count = int(entry.get())
            total_calories += count * calories
        except ValueError:
            pass
    total_label.config(text=f"Total: {total_calories} cal")
    insert_data(total_calories, id_entry)


# Function to reset all entries and the total label
def reset_entries(entries, total_label, id_entry):
    for entry in entries:
        entry.delete(0, tk.END)
    total_label.config(text="Total: 0 cal")
    id_entry.delete(0, tk.END)


# Function to switch to the first window
def open_first_window(current_root):
    current_root.destroy()
    subprocess.run(['python', 'system.py', ssn])


# Main function for the second window
def main_second():
    food_items = [
        ("Coffee with Milk & Sugar (1.0 cup)", 73),
        ("Tea with Milk & Sugar (1.0 cup)", 35),
        ("Milk (1.0 glass)", 167),
        ("Apple (1.0 large)", 131),
        ("Orange (1.0 fruit)", 62),
        ("Banana (1.0 small)", 90),
        ("Samosa (1.0 piece)", 349),
        ("Peanuts, Roasted (100 grams)", 567)
    ]

    bg_image_path = r"Assets\WhatsApp Image 2024-07-30 at 14.49.43_4ddfe8a6.jpg"

    root = initialize_window("Calorie Counter - Page 2")
    root.resizable(False, False)
    load_background(root, bg_image_path)

    entries = create_food_entries(root, food_items)

    '''id_label = tk.Label(root, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
    id_label.place(x=350, y=380)
    id_entry = tk.Entry(root, font=("Arial", 15), fg="#000", bg="#fff", width=10, highlightcolor='gray',
                        highlightthickness=5, highlightbackground='gray')
    id_entry.place(x=350, y=430)'''

    total_label = tk.Label(root, text="Total: 0 cal", fg="black", font=("Arial", 14))
    total_label.place(x=200, y=600)

    total_button = tk.Button(root, text="Total",
                             command=lambda: calculate_total(entries, food_items, total_label, ssn), bg="gray",
                             fg="black", font=("Arial", 12))
    total_button.place(x=200, y=550)

    reset_button = tk.Button(root, text="Reset", command=lambda: reset_entries(entries, total_label, ssn),
                             bg="gray", fg="black", font=("Arial", 12))
    reset_button.place(x=200, y=650)

    left_button = tk.Button(root, text="<<<", command=lambda: open_first_window(root), bg="black", fg="white",width=10,
                            font=("Arial", 12))
    left_button.place(x=10, y=650)

    root.mainloop()


if __name__ == "__main__":
    main_second()
