from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import subprocess 
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

cursor = conn.cursor()

def open_weight_loss_tips():
    try:
        cursor.execute("update visitors set diet_plan=? where visitor_SSN=?", ("loss weight", ssn))
        conn.commit()
        webbrowser.open('https://youtu.be/PDIBIz1XeQw?si=9X5XNiQsZoGnu5Wg')
        subprocess.Popen(['python', 'weight_loss_tips_page.py',ssn])
    except Exception as e:
        print(e)

def open_weight_gain_tips():
    try:
        cursor.execute("update visitors set diet_plan=? where visitor_SSN=?", ("gain weight", ssn))
        conn.commit()
        webbrowser.open('https://youtu.be/wRWSUKSTOHg?si=udSbvbQWJC7P1J6Z')
        subprocess.Popen(['python', 'gain_weight.py',ssn])
    except Exception as e:
        print(e)

def go_back():
    root.destroy()
    subprocess.Popen(['python', 'system.py',ssn])

# Main window
root = Tk()
root.resizable(False, False)
root.title("Diet Plan")
root.geometry('400x600')

# Use PIL to open and resize the background image
background_image_path = r"Assets\WhatsApp Image 2024-07-31 at 10.55.46_5b40fdba.jpg"
bg_img = Image.open(background_image_path)
bg_img_resized = bg_img.resize((400, 600), Image.LANCZOS)
diet = ImageTk.PhotoImage(bg_img_resized)

diet_image = Label(root, image=diet)
diet_image.place(relheight=1, relwidth=1)

# Set start label
custom_font = ("Comic Sans MS", 14, "italic")
start = Label(root, text="FITNESS OVER EVERYTHING", bg="#000", fg="gray", font=custom_font)
start.place(x=200, y=35, anchor='n')

'''id_label = Label(root, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.place(x=20, y=80)
id_entry = Entry(root, font=("Arial", 15), fg="#000", bg="#fff", width=10, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
id_entry.place(x=70, y=80)'''

# Load button background images
weight_loss_image_path = r"Assets\anastase-maragos-4dlhin0ghOk-unsplash.jpg"
weight_gain_image_path = r"Assets\anastase-maragos-9dzWZQWZMdE-unsplash.jpg"

# Use PIL to open and resize the images
weight_loss_img = Image.open(weight_loss_image_path)
weight_loss_img_resized = weight_loss_img.resize((275, 125), Image.LANCZOS)
weight_loss_photo = ImageTk.PhotoImage(weight_loss_img_resized)

weight_gain_img = Image.open(weight_gain_image_path)
weight_gain_img_resized = weight_gain_img.resize((275, 125), Image.LANCZOS)
weight_gain_photo = ImageTk.PhotoImage(weight_gain_img_resized)

# Create buttons with the resized background images and no borders
btn1 = Button(root, image=weight_loss_photo, text="Weight Loss", fg="gray", font="Helvetica 15 bold",
              compound=CENTER, bd=0, highlightthickness=0, command=open_weight_loss_tips)
btn1.place(x=60, y=150, width=275, height=125)

btn2 = Button(root, image=weight_gain_photo, text="Weight Gain", fg="gray", font="Helvetica 15 bold",
              compound=CENTER, bd=0, highlightthickness=0, command=open_weight_gain_tips)
btn2.place(x=60, y=350, width=275, height=125)

# Add back button with command to go back
btn = Button(root, text="<<<", fg="gray", font="Helvetica 15 bold", bg="black", bd=0, highlightthickness=0, command=go_back)
btn.place(x=30, y=525)

# Start the main loop
root.mainloop()

cursor.close()
conn.close()
