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
def dumbels():
    webbrowser.open('https://youtu.be/qqEw8XH-feI?si=2N-023P2gkEcgL4S')
    try:
        cursor.execute("INSERT INTO workouts (visitor_id,workout) VALUES (?,?)", (ssn, "Back dumbels only"))
        conn.commit()
    except Exception as e:
        print(e)

def widelats():
    webbrowser.open('https://youtu.be/lSyoAIi6DdU?si=S-4BsnEb_4CVz805')
    try:
        cursor.execute("INSERT INTO workouts (visitor_id,workout) VALUES (?,?)", (ssn,"back wide lats"))
        conn.commit()
    except Exception as e:
        print(e)

root = Tk()
root.title('BACK')
root.resizable(False, False)
font = ("Comic Sans MS", 15, "bold")
padx = 0
pady = 40

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
lbl_txt = Label(root, text='BE SAVAGE NOT AVERAGE', font=font, fg='gray', bg='black', padx=padx, pady=pady)
lbl_txt.pack(side='top')

'''id_label = Label(root, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.place( x=20, y=80)
id_entry = Entry(root, font=("Arial", 15), fg="#000", bg="#fff",width=10,highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
id_entry.place( x=70, y=80)'''

def open_link(url):
    webbrowser.open(url)

img_BACK = PhotoImage(file=r"Assets\BACK1.png")
BACK_btn = Button(root, image=img_BACK, text='', font=('Bold', 12), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=dumbels)
BACK_btn.place(width=350, height=150, x=20, y=140)

img_BACK2 = PhotoImage(file=r"Assets\BACK2.png")
BACK2_btn = Button(root, image=img_BACK2, text='', font=('Bold', 12), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=widelats)
BACK2_btn.place(width=350, height=150, x=20, y=320)

def go_back():
    root.destroy()
    subprocess.run(['python', 'workout.py',ssn])

exit_btn = Button(root, text='<<<', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=go_back)
exit_btn.place(width=70, height=30, x=20, y=550)

root.mainloop()
