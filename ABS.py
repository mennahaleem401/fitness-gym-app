from tkinter import *
from tkinter import ttk, PhotoImage
import subprocess  # To run other Python scripts
import webbrowser
import sqlite3
import sys
from globalvariables import AppController

conn = sqlite3.connect("GYMbd1.db")
cursor = conn.cursor()
root = Tk()
root.title('ABS')
font = ("Comic Sans MS", 15, "bold")
padx = 0
pady = 40

# Initialize the AppController and set the ssn
controller = AppController()
if len(sys.argv) > 1:
    ssn = sys.argv[1]
    print(ssn)
    controller.set_data("ssn", ssn)
else:
    print("Usage: python abs_page.py <ssn>")
    sys.exit(1)

def Strength():
    webbrowser.open('https://youtu.be/8PwoytUU06g?si=NuwqdzkbfnPj-Nih')
    try:
        cursor.execute("INSERT INTO workouts (visitor_id, workout) VALUES (?, ?)", (controller.get_data("ssn"), "Strength abs"))
        conn.commit()
    except Exception as e:
        print(e)

def Beginners():
    webbrowser.open('https://youtu.be/3p8EBPVZ2Iw?si=vvodBr-yJxsceotj')
    try:
        cursor.execute("INSERT INTO workouts (visitor_id, workout) VALUES (?, ?)", (controller.get_data("ssn"), "beginner abs"))
        conn.commit()
    except Exception as e:
        print(e)

def screen_center(w, h):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - w) / 2)
    y = int((screenheight - h) / 2)
    root.geometry(f"{w}x{h}+{x}+{y}")

screen_center(400, 600)
root.resizable(FALSE, FALSE)

def open_link(url):
    webbrowser.open(url)

wel = PhotoImage(file=r"Assets/background (2).png")
back = Label(root, image=wel).place(relheight=1, relwidth=1)
lbl_txt = Label(root, text='DO IT FOR AFTER SELFIE', font=font, fg='gray', bg='black', padx=padx, pady=pady)
lbl_txt.pack(side='top')

img_ABS1 = PhotoImage(file=r"Assets/ABS1.png")
ABS1_btn = Button(root, image=img_ABS1, text='', font=('Bold', 12), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=Strength)
ABS1_btn.place(width=350, height=150, x=20, y=140)

img_ABS2 = PhotoImage(file=r"Assets/ABS2.png")
ABS2_btn = Button(root, image=img_ABS2, text='', font=('Bold', 12), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=Beginners)
ABS2_btn.place(width=350, height=150, x=20, y=320)

def go_back():
    root.destroy()
    subprocess.run(['python', 'workout.py', ssn])

exit_btn = Button(root, text='<<<', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=go_back)
exit_btn.place(width=70, height=30, x=20, y=550)

root.mainloop()
