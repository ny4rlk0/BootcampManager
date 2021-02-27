#Code by Nyarlko 25.2.2021 all brands belongs to their respective owners.
#Main target of this software is Macbook Late 2006 but
#any mac runs Windows should be able to run this software.
#Use at your own risk!
#Special thx to stackoverflow.com/users/12172291/alexzander
import os,ctypes,sys,webbrowser,wx,wx.adv
import subprocess as sp
from pathlib import Path
import tkinter as ui
import psutil as ps
from tkinter import messagebox as mb
import time
CREATE_NO_WINDOW = 0x08000000
nya=0
rlko=0
file_path = __file__ #current file name
file_name = os.path.basename(__file__) #current file path + file name
b_stat="Updating status."
def get_admin():#REQUEST ADMIN
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return
    except:
        return False
def chk_admin(): #Returns true if we are admin false if we are not.
    try:
        is_admin=(os.getuid()==0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
def admin():
    global admin
    if chk_admin():
        admin=True
    else:
        admin=False
try:
    admin()
except:
    pass
window=ui.Tk()
window.title("Bootcamp Manager @nyarlko")
window.geometry("700x280")
window.resizable(0,0)
window.configure(bg="white")
def donate():
    newWindow = ui.Toplevel(window)
    newWindow.geometry("525x275")
    newWindow.resizable(0,0)
    labelExample = ui.Label(newWindow, text = "Any amount is appreciated.")
    donatee = ui.Text(newWindow)
    labelExample.pack()
    donatee.pack()
    donatee.insert(ui.END,"BTC: 3NhGAPpkLas1pDdPp7tSeP5ba1gHapq7kb")
    donatee.configure(state='disabled')
def remove_boot():
    try:
        sp.check_output(["schtasks","/delete","/tn","BOOTCAMP_MANAGER_BOOT","/f"])
        sp.check_output(["schtasks","/delete","/tn","BOOTCAMP_MANAGER_LOGIN","/f"])
        t.configure(text="Successfully removed from boot.",bg="green")
        mb.askquestion(title="Info", message="Restarting in 10 seconds.")
        os.system(r'shutdown -r -t 10')
    except:
        t.configure(text="Failed while removing from boot.",bg="red")
def add_boot():
    try:
        sp.check_output(["schtasks","/create","/sc","ONLOGON","/tn","BOOTCAMP_MANAGER_LOGIN","/tr","C:/Program Files/Boot Camp/Bootcamp.exe","/rl","HIGHEST"],creationflags=CREATE_NO_WINDOW).decode()
        sp.check_output(["schtasks","/create","/sc","ONSTART","/tn","BOOTCAMP_MANAGER_BOOT","/tr","C:/Program Files/Boot Camp/Bootcamp.exe","/rl","HIGHEST"],creationflags=CREATE_NO_WINDOW).decode()
        t.configure(text="Successfully added to boot.",bg="green")
        mb.askquestion(title="Info", message="Restarting in 10 seconds.")
        os.system(r'shutdown -r -t 10')
    except:
        t.configure(text="Failed while adding to boot.",bg="red")
def process_exists(process_name):
    if admin==True:
        out = sp.check_output(["TASKLIST","/FI","imagename eq Bootcamp.exe"],creationflags=CREATE_NO_WINDOW).decode()
        out = out.strip().split('\r\n')[-1]
        out = out.lower().startswith(process_name.lower())
        return out
try:
    t = ui.Label(text="",bg="white")
    t.pack()
except:
    pass
def restart_Bootcamp():
    if admin==True: #If run as administrator
        if process_exists('Bootcamp.exe'): #If Bootcamp is running
            os.system(r'taskkill /IM "Bootcamp.exe" /F') #kill Bootcamp
        sp.Popen([r"C:/Program Files/Boot Camp/Bootcamp.exe"]) #start Bootcamp (Hard coded bad bad bad... i should check windows install directory before but im too lazy.)
def bootcamp_Status_Update():
    try:
        if process_exists('Bootcamp.exe'):
            b_stat="Bootcamp is Running."
            bot.configure(text=b_stat,bg="green",fg="white")
            window.configure(bg="green")
            t.configure(bg="green")
        else:
            b_stat="Bootcamp has been stopped. Attempting to Restart."
            bot.configure(text=b_stat,bg="red",fg="white")
            window.configure(bg="red")
            t.configure(bg="red")
            restart_Bootcamp()
    except:
        pass
    window.after(1000,bootcamp_Status_Update)
if admin==True:
    button=ui.Button(
        text="Add to boot",
        width=20,
        height=1,
        bg="gold2",
        fg="white",
        command=add_boot,
    )
    button.pack()
    button2=ui.Button(
        text="Remove from boot",
        width=20,
        height=1,
        bg="cadetblue",
        fg="white",
        command=remove_boot,
    )
    button2.pack()
    button3=ui.Button(
        text="Restart Bootcamp",
        width=20,
        height=1,
        bg="blue4",
        fg="white",
        command=restart_Bootcamp,
    )
    button3.pack()
    button4=ui.Button(
        text="Donate",
        width=20,
        height=1,
        bg="orange",
        fg="white",
        command=donate,
    )
    button4.pack()
if admin==False: 
    warning_msg="Run Bootcamp Manager as Administrator!"
    warning_title="Important"
    mb.showerror(title=warning_title, message=warning_msg)
    sys.exit()  
if admin==True:
    bot = ui.Label(text=b_stat,bg="white")
    bot.pack()
if nya==rlko:
    window.configure(bg="white")
    window.after(1000,bootcamp_Status_Update)
    #window.withdraw() Hides window
    window.mainloop()
