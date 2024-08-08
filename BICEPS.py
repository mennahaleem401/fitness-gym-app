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
root.title('BICEPS')
font = ("Comic Sans MS", 15, "bold")
padx = 0
pady = 40

def dumbels_only():
    webbrowser.open('https://youtu.be/0mLMjPwQNkw?si=djPUrrGxBpUzZ_-Y')
    try:
        cursor.execute("INSERT INTO workouts (visitor_id,workout) VALUES (?,?)", (ssn, "arm dumbels only"))
        conn.commit()
    except Exception as e:
        print(e)

def bigger_arms():
    webbrowser.open('https://youtu.be/lBy-7EFK30o?si=Pm61sfZ1_TKMRL_9')
    try:
        cursor.execute("INSERT INTO workouts (visitor_id,workout) VALUES (?,?)", (ssn, "big arms"))
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
lbl_txt = Label(root, text='DONT SIT GET FIT', font=font, fg='gray', bg='black', padx=padx, pady=pady)
'''id_label = Label(root, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.place( x=20, y=80)
id_entry = Entry(root, font=("Arial", 15), fg="#000", bg="#fff",width=10,highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
id_entry.place( x=70, y=80)'''
lbl_txt.pack(side='top')

def open_link(url):
    webbrowser.open(url)

img_BI1 = PhotoImage(file=r"Assets\BI1.png")
BI1_btn = Button(root, image=img_BI1, text='', font=('Bold', 12), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=dumbels_only)
BI1_btn.place(width=350, height=150, x=20, y=140)

img_BI2 = PhotoImage(file=r"Assets\BI2.png")
BI2_btn = Button(root, image=img_BI2, text='', font=('Bold', 12), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=bigger_arms)
BI2_btn.place(width=350, height=150, x=20, y=320)

def go_back():
    root.destroy()
    subprocess.run(['python', 'workout.py',ssn])

exit_btn = Button(root, text='<<<', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=go_back)
exit_btn.place(width=70, height=30, x=20, y=550)

root.mainloop()
