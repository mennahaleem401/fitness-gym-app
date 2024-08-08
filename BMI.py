from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import sqlite3
import sys
from globalvariables import AppController

# Check if the argument is provided
if len(sys.argv) < 2:
    print("Usage: python BMI.py <ssn>")
    sys.exit(1)

ssn = sys.argv[1]
print(ssn)
# Initialize the AppController and set the ssn
controller = AppController()
controller.set_data("ssn", ssn)

conn = sqlite3.connect("GYMbd1.db")

def insert_data(result):
    try:
        weight_value = weight.get()
        height_value = height.get()
        cursor = conn.cursor()
        cursor.execute("UPDATE BMI set height=?, weight=? WHERE visitor_id=?", (height_value, weight_value, ssn))
        cursor.execute("update visitors set bmi=? where visitor_SSN=?", (result, ssn))
        conn.commit()
    except Exception as e:
        print(e)



def CalculateBtn():
    result = float(0)
    result = int(weight.get()) / ((int(height.get()) / 100) ** 2)
    mess = ""
    if result <= 18.5:
        mess = f"BMI Result: {result} it is Underweight"
    elif result > 18.5 and result <= 25:
        mess = f"BMI Result: {result} it is Normal"
    else:
        mess = f"BMI Result: {result} it is Overweight"
    messagebox.showinfo("Result", mess)
    insert_data(result)
    return int(result)

def resetfun():
    weight.delete(0, END)
    height.delete(0, END)
    return

# Main window setup
BMI = Tk()
def go_to_system():
    """Launches the system.py script when the back arrow is clicked."""
    BMI.destroy()
    subprocess.Popen(['python', 'system.py', ssn])

BMI.geometry('500x700')
BMI.title('BMI')
BMI.resizable(False, False)
# Background image setup
bg_image = Image.open(r"Assets/background2.png")
bg_photo = ImageTk.PhotoImage(bg_image, width=500, height=700)
bg_label = Label(BMI, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

mainframe = Frame(bg_label, background='black')

# Labels and Entries
lbl1 = Label(bg_label, text='DECIDE . COMMIT . SUCCEED', font=("Comic Sans MS", 15, 'bold'), fg='gray', background='black')
lbl1.grid(row=0, column=0, columnspan=2, padx=100, pady=45)

'''id_label = Label(bg_label, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.grid(row=1, column=0, padx=10, pady=10)
id_entry = Entry(bg_label, font=("Arial", 15), fg="#000", bg="#fff", width=10, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
id_entry.grid(row=1, column=1, padx=10, pady=10)'''

lbl3 = Label(bg_label, text='Enter Your Weight  (Kg)', font=('Arial', 13), fg='gray', bg='black')
lbl3.grid(row=2, column=0, pady=30)

weight = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
weight.grid(row=2, column=1, columnspan=2, pady=20)

lbl4 = Label(bg_label, text='Enter Your Height  (CM)', font=('Arial', 13), bg='black', fg='gray')
lbl4.grid(row=3, column=0, pady=20)

height = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
height.grid(row=3, column=1, pady=20)

# Buttons
btn1 = Button(bg_label, text='Calculate', command=CalculateBtn, width=20, height=2, background='black', fg='white', font=('Arial', 10))
btn1.grid(row=4, column=0, pady=50)

btn2 = Button(bg_label, text='Reset', command=resetfun, width=20, height=2, background='black', fg='white', font=('Arial', 10))
btn2.grid(row=4, column=1, pady=50)

btn3 = Button(bg_label, text='<<<', font=13, background="black", foreground="white", width=10, borderwidth=0, command=go_to_system)
btn3.grid(row=5, column=0, pady=180, sticky='nw', padx=10)

bg_label.place(relx=0.5, rely=0.5, anchor="c")

BMI.mainloop()
