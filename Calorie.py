from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os
import sys
from globalvariables import AppController

# Check if the argument is provided
if len(sys.argv) < 2:
    print("Usage: python calories.py <ssn>")
    sys.exit(1)

ssn = sys.argv[1]

# Initialize the AppController and set the ssn
controller = AppController()
controller.set_data("ssn", ssn)

def open_breakfastcalories():
    root.destroy()
    os.system(f'python breakfastCalories.py {ssn}')

def open_thirdwindow():
    root.destroy()
    os.system(f'python third_window.py {ssn}')

def open_secondwindow():
    root.destroy()
    subprocess.Popen(['python', 'second_window.py', ssn])

def open_firstwindow():
    root.destroy()
    subprocess.Popen(['python', 'first_window.py', ssn])

root = Tk()
root.geometry('500x700')
root.title('CALORIES')
root.resizable(False, False)

bg_image = Image.open(r"Assets/background2.png")
bg_photo = ImageTk.PhotoImage(bg_image, width=500, height=700)
bg_label = Label(root, image=bg_photo)

icon = Image.open(r"Assets/torso.png")
updicon = ImageTk.PhotoImage(icon)
icon_label = Label(bg_label, image=updicon, width=100, height=120, bg="black")

bg_label.place(x=0, y=0, relwidth=1, relheight=1)
lbl1 = Label(bg_label, text='LET . IT . BURN', font=("Comic Sans MS", 18, 'bold'), fg='gray', background='black')
lbl1.grid(row=0, column=0, columnspan=2, padx=5)
icon_label.grid(row=0, column=0)

bg_button1 = Button(bg_label, text='Breakfast', font=('Arial', 13), bg="black", fg='white', width=40, height=2, command=open_breakfastcalories)
bg_button2 = Button(bg_label, text='Morning Snack', font=('Arial', 13), bg="black", fg='white', width=40, height=2, command=open_thirdwindow)
bg_button3 = Button(bg_label, text='Lunch', font=('Arial', 13), bg="black", fg='white', width=40, height=2, command=open_firstwindow)
bg_button4 = Button(bg_label, text='Evening Snack', font=('Arial', 13), bg="black", fg='white', width=40, height=2, command=open_firstwindow)
bg_button5 = Button(bg_label, text='Dinner', font=('Arial', 13), bg="black", fg='white', width=40, height=2, command=open_secondwindow)

bg_button1.grid(row=2, column=0, columnspan=2, padx=60, pady=15)
bg_button2.grid(row=3, column=0, columnspan=2, padx=60, pady=15)
bg_button3.grid(row=4, column=0, columnspan=2, padx=60, pady=15)
bg_button4.grid(row=5, column=0, columnspan=2, padx=60, pady=15)
bg_button5.grid(row=6, column=0, columnspan=2, padx=60, pady=15)

btn3 = Button(bg_label, text='<<<', font=20, background="black", foreground="gray", width=10, borderwidth=0, command=open_thirdwindow)
btn3.grid(row=7, column=0, pady=60, padx=10, sticky='nw')

root.mainloop()
