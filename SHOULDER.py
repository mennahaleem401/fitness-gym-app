from tkinter import *
from tkinter import ttk, PhotoImage
import subprocess  # To run other Python scripts
import webbrowser
import sqlite3
import sys
from globalvariables import AppController


if len(sys.argv) < 2:
    print("Usage: python lunchCalories.py <ssn>")
    sys.exit(1)

ssn = sys.argv[1]
# Initialize the AppController and set the ssn
controller = AppController()
controller.set_data("ssn", ssn)
print(ssn)

conn=sqlite3.connect("GYMbd1.db")
cursor = conn.cursor()

root = Tk()
root.title('SHOULDER')
font = ("Comic Sans MS", 15, "bold")
padx = 0
pady = 40

def boulder():
    webbrowser.open('https://youtu.be/qNncOv3dJTg?si=kj5L3311PlxxkxZ8')
    try:
        cursor.execute("INSERT INTO workouts (visitor_id,workout) VALUES (?,?)", (ssn, "boulder"))
        conn.commit()
    except Exception as e:
        print(e)

def dumbels_only():
    webbrowser.open('https://youtu.be/g5oQZmk7xMc?si=_k7rXqnGkCIisyjp')
    try:
        cursor.execute("INSERT INTO workouts (visitor_id,workout) VALUES (?,?)", (ssn, "dumbels only"))
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

wel = PhotoImage(file=r"Assets\background (2).png")
back = Label(root, image=wel).place(relheight=1, relwidth=1)
lbl_txt = Label(root, text='EVERY WORKOUT COUNT', font=font, fg='gray', bg='black', padx=padx, pady=pady)
lbl_txt.pack(side='top')
'''id_label = Label(root, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.place( x=20, y=80)
id_entry = Entry(root, font=("Arial", 15), fg="#000", bg="#fff",width=10,highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
id_entry.place( x=70, y=80)'''

def open_link(url):
    webbrowser.open(url)

img_SH1 = PhotoImage(file=r"Assets\shoulder.png")
SH1_btn = Button(root, image=img_SH1, text='', font=('Bold', 12), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=boulder)
SH1_btn.place(width=350, height=150, x=20, y=140)


img_SH2 = PhotoImage(file=r"Assets\shoulder2.png")
SH2_btn = Button(root, image=img_SH2, text='', font=('Bold', 12), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=dumbels_only())
SH2_btn.place(width=350, height=150, x=20, y=320)


def go_back():
    root.destroy()
    subprocess.run(['python', 'workout.py',ssn])

exit_btn = Button(root, text='<<<', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=go_back)
exit_btn.place(width=70, height=30, x=20, y=550)

root.mainloop()
