import tkinter as ttk

import style as style

from squarcle import *

from tkinter.ttk import *

from Game import *

hm = HangMan

window = ttk.Tk()

canvas = ttk.Canvas(window, bg="#121212", bd=0, highlightthickness=0, width=900, height=300)
textBox = round_rectangle(0, 50, 900, 200, 'grey', canvas)
canvas.pack()

window.title("Python GUI App")
window.configure(bg='#121212')

# move window center
winWidth = 1000
winHeight = 600
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winHeight / 2)
window.geometry("{}x{}+{}+{}".format(winWidth, winHeight, posRight, posDown))
window.resizable(False, False)

DispLabel = ttk.Label(window, text='Are you a Geek?', font=('italic', 30), bg='grey', fg='white')
DispLabel.place(y=120, relx=0.5, anchor='center')


QButton = Button(window, text="Q", command=lambda: hm.hang_man(guess=QButton['text']))
QButton.place(y=250, x=30, height=50)


WButton = Button(window, text="W", command=lambda: hm.hang_man(guess=WButton['text']))
WButton.place(y=250, x=120, height=50)

EButton = Button(window, text="E", command=lambda: hm.hang_man(guess=EButton['text']))
EButton.place(y=250, x=210, height=50)

RButton = Button(window, text="R", command=lambda: hm.hang_man(guess=RButton['text']))
RButton.place(y=250, x=300, height=50)

TButton = Button(window, text="T", command=lambda: hm.hang_man(guess=TButton['text']))
TButton.place(y=250, x=390, height=50)

YButton = Button(window, text="Y", command=lambda: hm.hang_man(guess=YButton['text']))
YButton.place(y=250, x=480, height=50)

UButton = Button(window, text="U", command=lambda: hm.hang_man(guess=UButton['text']))
UButton.place(y=250, x=570, height=50)

IButton = Button(window, text="I", command=lambda: hm.hang_man(guess=IButton['text']))
IButton.place(y=250, x=660, height=50)

OButton = Button(window, text="O", command=lambda: hm.hang_man(guess=OButton['text']))
OButton.place(y=250, x=750, height=50)

PButton = Button(window, text="P", command=lambda: hm.hang_man(guess=PButton['text']))
PButton.place(y=250, x=840, height=50)

window.mainloop()
