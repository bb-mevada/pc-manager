from tkinter import *
import os
from tkinter import ttk

################# Window #####################
win = Tk()
win.geometry('350x320+550+200')
win.title('PC Manager')
win.resizable(False,False)
win.config(bg='white')
win.iconbitmap('Images/winicon.ico')

# Images
img1 = PhotoImage(file='Images/title.png')
img2 = PhotoImage(file='Images/devmgmt.png')
img3 = PhotoImage(file='Images/syspro.png')
img4 = PhotoImage(file='Images/network.png')
img5 = PhotoImage(file='Images/addrm.png')
img6 = PhotoImage(file='Images/mouse.png')
img7 = PhotoImage(file='Images/taskmgr.png')
img8 = PhotoImage(file='Images/group.png')
img9 = PhotoImage(file='Images/services.png')
img10 = PhotoImage(file='Images/panel.png')
img11 = PhotoImage(file='Images/registry.png')

################# Title #####################
win_title = Label(win,
text=' PC Manager',
image=img1,
compound='left',
font=('helvetica',25,'bold'),
bg='white',
fg='green',
bd=10,
relief=FLAT)
win_title.pack(fill='x')

# Styling object
s = ttk.Style()
s.configure('my.TButton',font=('arial',10,'bold'),anchor='w',width=18)

##################### Frame 1 ######################
frame_tools1 = Frame(win,bg='white',bd=2)

# Device Manager
btn_devmgmt = ttk.Button(frame_tools1,
text='Device Manager',
image=img2,
compound='left',
style='my.TButton',
command=lambda : os.system('devmgmt.msc'))

# System Properties
btn_syspro = ttk.Button(frame_tools1,
text='System Properties',
image=img3,
compound='left',
style='my.TButton',
command=lambda : os.system('sysdm.cpl'))

# Network Setup
btn_network = ttk.Button(frame_tools1,
text='Network Setting',
image=img4,
compound='left',
style='my.TButton',
command=lambda : os.system('ncpa.cpl'))

# Add or Remove
btn_addrm = ttk.Button(frame_tools1,
text='Add or Remove',
image=img5,
compound='left',
style='my.TButton',
command=lambda : os.system('appwiz.cpl'))

# Mouse Setting
btn_mouse = ttk.Button(frame_tools1,
text='Mouse Setting',
image=img6,
compound='left',
style='my.TButton',
command=lambda : os.system('main.cpl'))

btn_devmgmt.pack(pady=(0,5))
btn_syspro.pack(pady=(0,5))
btn_network.pack(pady=(0,5))
btn_addrm.pack(pady=(0,5))
btn_mouse.pack(pady=(0,5))
frame_tools1.pack(side='left')

##################### Frame 2 ######################
frame_tools2 = Frame(win,bg='white',bd=2)

# Task Manager
btn_taskmgr = ttk.Button(frame_tools2,
text='Task Manager',
image=img7,
compound='left',
style='my.TButton',
command=lambda : os.system('taskmgr'))

# Group Policy Editor
btn_group = ttk.Button(frame_tools2,
text='Group Policy Editor',
image=img8,
compound='left',
style='my.TButton',
command=lambda : os.system('gpedit.msc'))

# Services
btn_services = ttk.Button(frame_tools2,
text='System Services',
image=img9,
compound='left',
style='my.TButton',
command=lambda : os.system('services.msc'))

# Control Panel
btn_panel = ttk.Button(frame_tools2,
text='Control Panel',
image=img10,
compound='left',
style='my.TButton',
command=lambda : os.system('control'))

# Registry
btn_registry = ttk.Button(frame_tools2,
text='Registry Editor',
image=img11,
compound='left',
style='my.TButton',
command=lambda : os.system('regedit'))

btn_taskmgr.pack(pady=(0,5))
btn_group.pack(pady=(0,5))
btn_services.pack(pady=(0,5))
btn_panel.pack(pady=(0,5))
btn_registry.pack(pady=(0,5))
frame_tools2.pack(side='right')

mainloop()