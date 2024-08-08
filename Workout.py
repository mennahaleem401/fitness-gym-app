from tkinter import *
from tkinter import ttk, PhotoImage
import subprocess  # To run other Python scripts
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
root = Tk()
root.title('Workout')
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
root.resizable(False, False)

def go_back():
    root.destroy()
    subprocess.run(['python', 'system.py',ssn])

wel = PhotoImage(file=r"Assets/background (2).png")
back = Label(root, image=wel).place(relheight=1, relwidth=1)
lbl_txt = Label(root, text='HUSTLE FOR THAT MUSCLE', font=font, fg='gray', bg='black', padx=padx, pady=pady)
lbl_txt.pack(side='top')

def open_script(script_name):
    root.destroy()
    subprocess.run(['python', script_name,ssn])

img_chest = PhotoImage(file=r"Assets/WORKOUT.png")
chest_btn = Button(root, image=img_chest, text='CHEST', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=lambda: open_script('CHEST.py'))
chest_btn.place(width=170, height=90, x=20, y=150)

img_back = PhotoImage(file=r"Assets/WORKOUT.png")
back_btn = Button(root, image=img_back, text='BACK', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=lambda: open_script('BACK.py'))
back_btn.place(width=170, height=90, x=200, y=150)

img_BICEPS = PhotoImage(file=r"Assets/WORKOUT.png")
BICEPS_btn = Button(root, image=img_BICEPS, text='BICEPS', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=lambda: open_script('BICEPS.py'))
BICEPS_btn.place(width=170, height=90, x=20, y=270)

img_SQUAT = PhotoImage(file=r"Assets/WORKOUT.png")
SQUAT_btn = Button(root, image=img_SQUAT, text='SQUAT', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=lambda: open_script('SQUAT.py'))
SQUAT_btn.place(width=170, height=90, x=200, y=270)

img_SHOULDER = PhotoImage(file=r"Assets/WORKOUT.png")
SHOULDER_btn = Button(root, image=img_SHOULDER, text='SHOULDER', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=lambda: open_script('SHOULDER.py'))
SHOULDER_btn.place(width=170, height=90, x=20, y=390)

img_ABS = PhotoImage(file=r"Assets/WORKOUT.png")
ABS_btn = Button(root, image=img_ABS, text='ABS', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=lambda: open_script('ABS.py'))
ABS_btn.place(width=170, height=90, x=200, y=390)

exit_btn = Button(root, text='<<<', font=('Bold', 22), fg='gray', bg='black', compound=CENTER, bd=5, highlightthickness=0, cursor='hand2', command=go_back)
exit_btn.place(width=70, height=30, x=20, y=550)

root.mainloop()
