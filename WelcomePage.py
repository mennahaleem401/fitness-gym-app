# welcome_page.py
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import date
from tkinter import messagebox
import subprocess
from globalvariables import AppController
import sqlite3
def open_system(controller):
    if insert_data(controller) > 0:
        ssn = controller.get_data("ssn")
        subprocess.Popen(['python', 'system.py', ssn])
    else:
        messagebox.showerror("ERROR", "Please enter Name and ID ")

def insert_data(controller):
    try:
        ssn = controller.get_data("ssn")
        name = controller.get_data("name")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitors (visitor_name, visitor_SSN, dateOfDay) VALUES (?, ?, ?)",
                       (name, ssn, date_combobox.get()))
        cursor.execute("INSERT INTO BMI (visitor_id) VALUES (?)", (ssn,))
        cursor.execute("INSERT INTO calories (visitor_id) VALUES (?)", (ssn,))
        conn.commit()
        return 1
    except Exception as e:
        print("Error:", e)
        return 0

conn = sqlite3.connect("GYMbd1.db")

controller = AppController()

root = Tk()
root.title("Welcome Page")
root.geometry("400x600")
root.resizable(False, False)

image_path = "Assets/background (2).png"
img = Image.open(image_path)
wel = ImageTk.PhotoImage(img)

back = Label(root, image=wel).place(relheight=1, relwidth=1)

custom_font = ("Comic Sans MS", 14, "italic")
label_one = Label(root, text="It's time to wake up the monster", font=custom_font, fg="gray", bg="#000").place(x=50, y=50)

eat = Label(root, text="Eat ", font=("Arial", 15), fg="gray", bg="#000").place(x=60, y=150)
dash1 = Label(root, text="-", font=("Arial", 20), fg="red", bg="#000").place(x=100, y=145)
sleep = Label(root, text="Sleep", font=("Arial", 15), fg="gray", bg="#000").place(x=120, y=150)
dash2 = Label(root, text="-", font=("Arial", 20), fg="red", bg="#000").place(x=180, y=145)
gym = Label(root, text="Gym", font=("Arial", 15), fg="gray", bg="#000").place(x=200, y=150)
dash3 = Label(root, text="-", font=("Arial", 20), fg="red", bg="#000").place(x=255, y=145)
repeat = Label(root, text="Repeat", font=("Arial", 15), fg="gray", bg="#000").place(x=280, y=150)

name_label = Label(root, text="Name:", font=("Arial", 15), fg="gray", bg="#000")
name_label.place(x=60, y=250)

name_entry = Entry(root, font=("Arial", 15), fg="#000", bg="#fff")
name_entry.place(x=140, y=250)

id_label = Label(root, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.place(x=60, y=300)

id_entry = Entry(root, font=("Arial", 15), fg="#000", bg="#fff")
id_entry.place(x=140, y=300)

data_label = Label(root, text="Data : ", font=("Arial", 15), fg="gray", bg="#000").place(x=60, y=350)

date_combobox = ttk.Combobox(root)
date_combobox.place(x=140, y=350, relwidth=0.56, relheight=0.045)

current_date = date.today()
date_combobox.set(current_date.strftime("%Y-%m-%d"))

def on_next():
    controller.set_data("ssn", id_entry.get())
    controller.set_data("name", name_entry.get())
    open_system(controller)

btn = Button(root, text=">>>", fg="gray", font="Helvetica 15 bold", bg="#000", highlightthickness=0, bd=0, command=on_next)
btn.place(x=330, y=525)

root.mainloop()
