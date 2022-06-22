import importlib.util
import os
import sys
import tkinter as tk
import tkinter as ttk
from tkinter.ttk import *
from RandomWord import random_word
from squarcle import *

# to display the splash screen when executing the program
if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
    import pyi_splash
    pyi_splash.update_text('UI Loaded ...')
    pyi_splash.close()

# declaring window
window = ttk.Tk()

# to get the location of the images used in the file when using --onefile method to prepare an executable
try:
    os.chdir(sys._MEIPASS)
    icon_path = 'images/hangman.png'
    light_path = 'images/light_mode.png'
    dark_path = 'images/night_mode.png'
except AttributeError:
    icon = ttk.PhotoImage(file='images/hangman.png')
else:
    icon = ttk.PhotoImage(file=icon_path)
window.iconphoto(False, icon)
canvas = ttk.Canvas(window, bg="#121212", bd=0, highlightthickness=0, width=900, height=300)
textBox = round_rectangle(0, 50, 900, 200, '#1f1f1f', canvas)
canvas.pack()

# color
primary_color = '#BB86FC'
life_color = '#CF6679'
background_color = '#1f1f1f'
flag = 0

try:
    photo = tk.PhotoImage(file=r"images/night_mode.png")
except:
    photo = tk.PhotoImage(file=dark_path)

theme_button = ttk.Button(bg=background_color, image=photo, width=50, command=lambda: light_theme())
theme_button.place(y=550, x=560, anchor='center')


def dark_theme():
    global background_color, textBox, primary_color, photo, theme_button, disp_label
    primary_color = '#BB86FC'
    background_color = '#1f1f1f'
    window.configure(bg='#121212')
    canvas.configure(bg='#121212')
    textBox = round_rectangle(0, 50, 900, 200, background_color, canvas)
    disp_label.configure(bg=background_color, fg=primary_color)
    won_label.configure(bg=background_color)
    retry_label.configure(bg=background_color)
    life_label.configure(bg=background_color)
    try:
        photo = tk.PhotoImage(file=r"images/night_mode.png")
    except:
        photo = tk.PhotoImage(file=dark_path)
    theme_button = ttk.Button(bg=background_color, image=photo, width=50, command=lambda: light_theme())
    theme_button.place(y=550, x=560, anchor='center')


def light_theme():
    global background_color, textBox, primary_color, theme_button, photo
    primary_color = '#00203f'
    background_color = '#adefd1'
    window.configure(bg='white')
    canvas.configure(bg='WHITE')
    textBox = round_rectangle(0, 50, 900, 200, background_color, canvas)
    disp_label.configure(bg=background_color, fg=primary_color)
    won_label.configure(bg=background_color)
    retry_label.configure(bg=background_color)
    life_label.configure(bg=background_color)
    try:
        photo = tk.PhotoImage(file=r"images/light_mode.png")
    except:
        photo = tk.PhotoImage(file=light_path)
    theme_button.place_forget()
    theme_button.configure(bg=background_color, image=photo, width=50, command=lambda: dark_theme())
    theme_button.place(y=550, x=560, anchor='center')
    disp_label.place()


# global variable declaration
j = 0
win = 0
count = 0
ges_word = []
str1 = ''
word = ''
entered_letter = []
list_ = 1
# total five life left
life = 5

retry_label = ttk.Label()
disp_label = ttk.Label()
won_label = ttk.Label()
life_label = ttk.Label()


def select_function(guess):
    if life == 0:
        retry_label.place_forget()
        won_label.place_forget()
        start()
    else:
        hang_man(guess)


def start():
    # word = random.choice(lst)  # SELECTING A RANDOM WORD FROM word_list.py
    global word, life, j, win, count, ges_word, entered_letter, disp_label, life_label
    j = 0
    win = 0
    count = 0
    ges_word = []
    word = ''
    life = 5
    # selecting a random word
    word = str(random_word())
    won_label.place_forget()
    retry_label.place_forget()
    entered_letter = []

    for i in word:
        if i.isalpha():
            ges_word.append('_')  # (_ _ _ ......)
            entered_letter.append(' ')
            entered_letter.append(' ')
            # LENGTH OF STRING
            j += 1

    disp_label = ttk.Label(window, text=' '.join(ges_word), font=('italic', 30), bg=background_color, fg=primary_color,
                           width=35)
    disp_label.place(y=120, relx=0.5, anchor='center')
    life_label = ttk.Label(window, text="LIFE = " + str(life), font=('italic', 15), bg=background_color, fg=life_color)
    life_label.place(y=70, x=900, anchor='center')


def hang_man(guess):
    global j, life, win, count, ges_word, entered_letter, disp_label, retry_label, won_label, life_label

    for char in range(j):
        # to check all elements in word
        if guess.lower() == word[char]:  # checking our guess is
            ges_word[char] = word[char]  # assigning the correct word to the char th position of ges_word
            win += 1  # counting number of wins

    if win == count:  # if guess is wrong
        life -= 1
        life_label = ttk.Label(window, text="LIFE = " + str(life), font=('italic', 15), bg=background_color,
                               fg=life_color)
        life_label.place(y=70, x=900, anchor='center')
    elif guess in entered_letter:
        win -= 1
    else:
        entered_letter[win] = guess

    # assigning number of wins to count
    count = int(win)

    disp_label = ttk.Label(window, text=' '.join(ges_word), font=('italic', 30,), bg=background_color, fg=primary_color,
                           width=35)
    disp_label.place(y=120, relx=0.5, anchor='center')
    if life == 0:
        disp_label.place_forget()
        retry_label = ttk.Label(window, text="The word was : " + word + "\nPress any button to RETRY",
                                font=('Arial', 25),
                                bg=background_color, fg=primary_color)
        retry_label.place(y=120, relx=0.5, anchor='center')
    elif win == j:
        disp_label.place_forget()
        won_label = ttk.Label(window, text="\nYOU WON!", font=('Arial', 25), bg=background_color, fg=primary_color)
        won_label.place(y=145, relx=0.5, anchor='center')
        disp_label.place_forget()
        disp_word = ttk.Label(window, text=' '.join(ges_word), font=('italic', 25,), bg=background_color, fg='#03DAC6')
        disp_word.place(y=110, relx=0.5, anchor='center')


# display
window.title("Python GUI App")
window.configure(bg='#121212')

# move window center
winWidth = 1000
winHeight = 600
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winHeight / 2)
window.geometry("{}x{}+{}+{}".format(winWidth, winHeight, posRight, posDown))
window.resizable(False, False)

start()

# row 1
QButton = Button(window, text="Q", command=lambda: select_function(guess=QButton['text']))
QButton.place(y=250, x=50, height=50)

WButton = Button(window, text="W", command=lambda: select_function(guess=WButton['text']))
WButton.place(y=250, x=140, height=50)

EButton = Button(window, text="E", command=lambda: select_function(guess=EButton['text']))
EButton.place(y=250, x=230, height=50)

RButton = Button(window, text="R", command=lambda: select_function(guess=RButton['text']))
RButton.place(y=250, x=320, height=50)

TButton = Button(window, text="T", command=lambda: select_function(guess=TButton['text']))
TButton.place(y=250, x=410, height=50)

YButton = Button(window, text="Y", command=lambda: select_function(guess=YButton['text']))
YButton.place(y=250, x=500, height=50)

UButton = Button(window, text="U", command=lambda: select_function(guess=UButton['text']))
UButton.place(y=250, x=590, height=50)

IButton = Button(window, text="I", command=lambda: select_function(guess=IButton['text']))
IButton.place(y=250, x=680, height=50)

OButton = Button(window, text="O", command=lambda: select_function(guess=OButton['text']))
OButton.place(y=250, x=770, height=50)

PButton = Button(window, text="P", command=lambda: select_function(guess=PButton['text']))
PButton.place(y=250, x=860, height=50)

# row 2
AButton = Button(window, text="A", command=lambda: select_function(guess=AButton['text']))
AButton.place(y=350, x=100, height=50)

SButton = Button(window, text="S", command=lambda: select_function(guess=SButton['text']))
SButton.place(y=350, x=190, height=50)

DButton = Button(window, text="D", command=lambda: select_function(guess=DButton['text']))
DButton.place(y=350, x=280, height=50)

FButton = Button(window, text="F", command=lambda: select_function(guess=FButton['text']))
FButton.place(y=350, x=370, height=50)

GButton = Button(window, text="G", command=lambda: select_function(guess=GButton['text']))
GButton.place(y=350, x=460, height=50)

HButton = Button(window, text="H", command=lambda: select_function(guess=HButton['text']))
HButton.place(y=350, x=550, height=50)

JButton = Button(window, text="J", command=lambda: select_function(guess=JButton['text']))
JButton.place(y=350, x=640, height=50)

KButton = Button(window, text="K", command=lambda: select_function(guess=KButton['text']))
KButton.place(y=350, x=730, height=50)

LButton = Button(window, text="L", command=lambda: select_function(guess=LButton['text']))
LButton.place(y=350, x=820, height=50)

# ROW 2
ZButton = Button(window, text="Z", command=lambda: select_function(guess=ZButton['text']))
ZButton.place(y=450, x=190, height=50)

XButton = Button(window, text="X", command=lambda: select_function(guess=XButton['text']))
XButton.place(y=450, x=280, height=50)

CButton = Button(window, text="C", command=lambda: select_function(guess=CButton['text']))
CButton.place(y=450, x=370, height=50)

VButton = Button(window, text="V", command=lambda: select_function(guess=VButton['text']))
VButton.place(y=450, x=460, height=50)

BButton = Button(window, text="B", command=lambda: select_function(guess=BButton['text']))
BButton.place(y=450, x=550, height=50)

NButton = Button(window, text="N", command=lambda: select_function(guess=NButton['text']))
NButton.place(y=450, x=640, height=50)

MButton = Button(window, text="M", command=lambda: select_function(guess=MButton['text']))
MButton.place(y=450, x=730, height=50)

# row 3
retry_button = tk.Button(text="RETRY", bg="red",
                         command=lambda: start())
retry_button.place(y=550, x=460, anchor='center')

window.mainloop()
