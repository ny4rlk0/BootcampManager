#/bin/bash
#Code by Nyarlko 25.2.2021 all brands belongs to their respective owners.
#Main target of this software is Macbook Late 2006 but
#any mac runs Windows should be able to run this software.
#Use at your own risk!
import os,ctypes,sys,wx,wx.adv,webbrowser
import subprocess as sp
from pathlib import Path
import tkinter as ui
import psutil as ps
from tkinter import messagebox as mb
import time
nya=0
rlko=0
file_path = __file__ #current file name
file_name = os.path.basename(__file__) #current file path + file name
b_stat="Updating status."
TRAY_TOOLTIP = 'Bootcamp Manager'
TRAY_ICON = 'app.ico'
def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Github <3', self.on_hello)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):      
        if nya==rlk0:
            echo=1+1
            
    def on_hello(self, event):
        webbrowser.open(url="https://github.com/ny4rlk0/BootcampManager")

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()

class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True

def main():
    app = App(False)
    app.MainLoop()

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
def remove_boot():
    try:
        os.system(r'xcopy %s C:/' % ('file'))
        os.chdir(r'C:/')
        os.system(r'attrib %s +h' % ('file'))
        os.system(r'schtasks /delete /tn BOOTCAMP_HANDLER /f')
        t.configure(text="Successfully removed from boot.",bg="green")
        mb.askquestion(title="Info", message="Restarting in 10 seconds.")
        os.system(r'reboot -r -t 10')
    except:
        t.configure(text="Failed while removing from boot.",bg="red")
def add_boot():
    try:
        os.system(r'xcopy %s C:/' % ('file'))
        os.chdir(r'C:/')
        os.system(r'attrib %s -h' % ('file'))
        c="C:/"
        target_dir=str(c)+str(file_name)
        os.system(r'schtasks /create /sc ONLOGON /tn BOOTCAMP_HANDLER /tr %s ' % ('target_dir'))
        t.configure(text="Successfully added to boot.",bg="green")
        mb.askquestion(title="Info", message="Restarting in 10 seconds.")
        os.system(r'reboot -r -t 10')
    except:
        t.configure(text="Failed while adding to boot.",bg="red")
def process_exists(process_name):
    if admin==True:
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        # use buildin check_output right away
        output = sp.check_output(call).decode()
        # check in last line for process name
        last_line = output.strip().split('\r\n')[-1]
        # because Fail message could be translated
        return last_line.lower().startswith(process_name.lower())

window=ui.Tk()
window.title("Bootcamp Manager @nyarlko")
window.geometry("550x225")
window.resizable(0,0)
window.configure(bg="white")
try:
    t = ui.Label(text="",bg="white")
    t.pack()
except:
    pass
def restart_Bootcamp():
    if admin==True: #If run as administrator
        if Bootcamp_status==True: #If Bootcamp is running
            os.system(r'taskkill /IM "Bootcamp.exe" /F') #kill Bootcamp
        sp.Popen([r"C:/Program Files/Boot Camp/Bootcamp.exe"]) #start Bootcamp (Hard coded bad bad bad... i should check windows install directory before but im too lazy.)
def bootcamp_Status_Update():
    try:
        global Bootcamp_status,b_stat
        Bootcamp_status=process_exists('Bootcamp.exe')#Check Bootcamp running true or false
        if Bootcamp_status==True:
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
    window.after(2000,bootcamp_Status_Update)
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
if admin==False:
    warning_msg="Run Bootcamp Handler as administrator!"
    warning_title="Important"
    mb.showerror(title=warning_title, message=warning_msg)
    sys.exit(0)
if admin==True:
    bot = ui.Label(text=b_stat,bg="white")
    bot.pack()
window.configure(bg="white")
window.after(2000,bootcamp_Status_Update)
window.mainloop()
if __name__ == '__main__':
    main()