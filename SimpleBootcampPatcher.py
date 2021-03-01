#Code by Nyarlko 25.2.2021 all brands belongs to their respective owners.
import os,sys
import tkinter as ui
from tkinter import messagebox as mb
CREATE_NO_WINDOW = 0x08000000
DIR=f"\"C://Program Files//Boot Camp//Bootcamp.exe\""
BB=f"\"BOOTCAMP_MANAGER_BOOT\""
BL=f"\"BOOTCAMP_MANAGER_LOGIN\""
window=ui.Tk()
window.title("Bootcamp Manager")
window.geometry("625x175")
window.resizable(0,0)
window.configure(bg="white")
def donate():
    newWindow = ui.Toplevel(window)
    newWindow.geometry("525x275")
    newWindow.resizable(0,0)
    labelExample = ui.Label(newWindow, text = "Any amount is appreciated. @nyarlko")
    donatee = ui.Text(newWindow)
    labelExample.pack()
    donatee.pack()
    donatee.insert(ui.END,"BTC: 3NhGAPpkLas1pDdPp7tSeP5ba1gHapq7kb")
    donatee.configure(state='disabled')
def patch():
    try:
        button.config(text='PATCHING..',bg='red',fg='white',state='disabled')
        os.system(f"schtasks /create /sc ONLOGON /tn {BL} /tr {DIR} /rl HIGHEST")
        os.system(f"schtasks /create /sc ONSTART /tn {BB} /tr {DIR} /rl HIGHEST")
    except:
        mb.showerror(title='Error',message='This computer seems like already patched!')
        sys.exit()
    else:
        button.config(state='active')
        button.config(text='PATCHED')
        button.config(state='disabled')
        mb.showinfo(title="Done",message="Patched.")
button=ui.Button(
    text="Patch",
    width=20,
    height=1,
    bg="green",
    fg="white",
    command=patch,
)
button.place(x=200,y=25)
button4=ui.Button(
    text="Donate",
    width=20,
    height=1,
    bg="orange",
    fg="white",
    command=donate,
)
button4.place(x=200,y=100)
window.configure(bg="black")
window.mainloop()
