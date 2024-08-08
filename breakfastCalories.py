from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import sqlite3
import sys
from globalvariables import AppController

# Check if the argument is provided
if len(sys.argv) < 2:
    print("Usage: python breakfastCalories.py <ssn>")
    sys.exit(1)

ssn = sys.argv[1]
print(ssn)

# Initialize the AppController and set the ssn
controller = AppController()
controller.set_data("ssn", ssn)

conn = sqlite3.connect("GYMbd1.db")


def insert_data(result):
    ssn = controller.get_data("ssn")
    cursor = conn.cursor()
    cursor.execute("UPDATE calories set morning_cal=? WHERE visitor_id=?", (result, ssn))
    conn.commit()


def go_back_to_system():
    root.destroy()
    subprocess.run(['python', 'system.py', ssn])


def CalculateBtn():
    entries = [txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9]
    calories = [17, 357, 112, 378, 539, 86, 82, 357, 49]

    total = 0
    for entry, cal in zip(entries, calories):
        try:
            value = int(entry.get())
        except ValueError:
            value = 0
        total += value * cal

    mess = f'The Total calories at breakfast = {total}'
    messagebox.showinfo("Total", mess)
    insert_data(total)
    return total


def resetfun():
    for entry in [txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9]:
        entry.delete(0, END)
    return


root = Tk()
root.geometry('500x700')
root.title('BREAKFAST')
root.resizable(False, False)

bg_image = Image.open(r"Assets/background2.png")
bg_photo = ImageTk.PhotoImage(bg_image, width=500, height=700)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

'''id_label = Label(bg_label, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(bg_label, font=("Arial", 15), fg="#000", bg="#fff", width=10, highlightcolor='gray',
                 highlightthickness=5, highlightbackground='gray')
id_entry.grid(row=0, column=1, padx=10, pady=10)'''

labels_texts = [
    'Cooked Egg Whites: ~17 calories',
    'Bacon on Biscuit: ~357 calories',
    'Cheese Biscuit: ~112 calories',
    'Egg and Bacon Biscuit: ~378 calories',
    'Sausage, Egg : ~539 calories',
    '1 Plain Pancake (4"): ~86 calories',
    'Pineapple: ~82 calories (1 cup chunks)',
    'Blueberries: ~84 calories (1 cup)',
    'Strawberries: ~49 calories (1 cup)'
]

entries = [txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9] = [
    Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray') for _ in
    range(9)]

for i, (label_text, entry) in enumerate(zip(labels_texts, entries), start=1):
    label = Label(bg_label, text=label_text, font=('Arial', 10), fg='gray', background='black')
    label.grid(row=i, column=0, pady=10)
    entry.grid(row=i, column=1, pady=10)


btn1 = Button(bg_label, text='Total', command=CalculateBtn, width=20, height=2, background='black', fg='white', font=('Arial', 10))
btn1.grid(row=10, column=0, pady=30)
btn2 = Button(bg_label, text='Reset', command=resetfun, width=20, height=2, background='black', fg='white', font=('Arial', 10))
btn2.grid(row=10, column=1, pady=30)

# Back arrow button with command to go back to system.py
btn3 = Button(bg_label, text='<<<', font=13, background="black", foreground="gray", width=10, borderwidth=0, command=go_back_to_system)
btn3.grid(row=11, column=0, pady=30, sticky='nw', padx=10)

root.mainloop()
