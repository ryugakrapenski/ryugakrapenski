import random
import pyautogui
import keyboard
from tkinter import *
import time
import win32api, win32con
from PIL import Image, ImageTk, ImageGrab

#Click Function
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.01)

#Main window and C Canvas
root = Tk()
root.title('Exerium')
root.geometry('300x300')
c = Canvas(root, width = 300, height = 300, bg = "red4")
c.pack()

#Create a circle function
def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill = "white", outline = "")

create_circle(150, 150, 75, c)

#Switching from start menu to main menu
def startmenu():
    #Destroy C Canvas
    c.destroy()
    #Create D Canvas
    d = Canvas(root, width = 300, height = 300, bg = 'seashell3')
    d.pack()
    #D Canvas welcome message
    welcome = Label(width = 200, height = 50, font = 'Courier', text = 'Welcome to RAC')
    d.create_window(150, 70, window = welcome)
    #D Canvas enter hotkey
    hotkeybox = Entry(root, justify = 'center')
    d.create_window(150, 150, window = hotkeybox)

    # Get hotkey button
    def gethotkey():
        global hotkey
        hotkey = hotkeybox.get()

    #D Canvas get hotkey
    gethotkeybutton = Button(root, width = 9, font = ('arial', 7), text = 'Enter Hotkey', bg = 'light blue', command = gethotkey)
    d.create_window(150, 180, window = gethotkeybutton)

    # Start Button
    start = Button(text='Start', height = 1, width = 10, font = 2, bg = 'pink', command=autoclicker)
    d.create_window(150, 250, window=start)

# Main Menu GUI
EXERIUM = Image.open("C:\\Users\\tyler\\PycharmProjects\\Personal\\venv\\exerium.png")
EXERIUMSMALL = EXERIUM.resize((100, 100))
imgexerium = ImageTk.PhotoImage(EXERIUMSMALL)
EXERIUM1 = Button(root, text="", image=imgexerium, highlightthickness=0, bd=0, command=startmenu)
c.create_window(150, 150, window=EXERIUM1)

#Auto Clicker Function
def autoclicker():
    while True:
        if keyboard.is_pressed('del'):
            exit(5)
        if keyboard.is_pressed(hotkey):
            for i in range(20):
                x = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
                y = random.choice(x)
                click()
                time.sleep(y)

root.mainloop()



