import tkinter as ttk

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

DispLabel = ttk.Label(window, text='Are you a Geek?', font=('italic', 30), bg='grey', fg='white')
DispLabel.place(y=120, relx=0.5, anchor='center')

aButton = Button(window, text="A", command=lambda: hm.hang_man(guess=aButton['text']))
aButton.pack()
window.mainloop()
