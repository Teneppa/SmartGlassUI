import sys
import os

from tkinter import *
from tkinter import font as tkFont
from pynput import keyboard

# Create the tkinter window
root = Tk()
#root.state('zoomed')
root.attributes('-fullscreen', True)

def chrome():
    os.system("kweb -KEJ 10.0.0.115:5000/video &")
    hide()

def hide():
    global hidden

    root.withdraw()
    hidden = True
    print("> hide window")

def show():
    global hidden

    # KILL ALL PROCESSES
    os.system("pkill kweb")

    root.deiconify()
    #root.state('zoomed')
    root.attributes('-fullscreen', True)
    hidden = False
    print("> show window")

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

        if key == key.ctrl_l:
            show()

for i in range(0, 2):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1, )

helv = tkFont.Font(family='Helvetica', size=20, weight='bold')

# Create button to hide
button = Button(background="#BFC9CA", text="HIDE", font=helv, command=hide)
button.grid(row=0,column=0,sticky=N+S+E+W)

# Create button to open chrome
button2 = Button(background="#E74C3C", text="CHROME", font=helv, command=chrome)
button2.grid(row=0,column=1,sticky=N+S+E+W)

# Create button to 
button = Button(background="#A9DFBF", text="?", font=helv, command=print())
button.grid(row=1,column=0,sticky=N+S+E+W)

# Create button to 
button2 = Button(background="#1ABC9C", text="?", font=helv, command=print())
button2.grid(row=1,column=1,sticky=N+S+E+W)

hidden = False

try:
    while True:
        root.update_idletasks()
        root.update()

        # If the window is hidden, wait for CTRL to be pressed
        # and then show the window again
        if hidden:
            with keyboard.Events() as events:
                # Block at most one second
                event = events.get(1.0)
                if event is None:
                    pass
                    #print('You did not press a key within one second')
                else:
                    print('Received event {}'.format(event))
                    print(event.key)
                    if event.key == event.key.ctrl_l:
                        print("CTRL")
                        show()

except Exception as e:
    os.system("pkill kweb")
    print(f"CYA: {e}")
    
