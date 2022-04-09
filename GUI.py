import tkinter as tk
#import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from Gymgather import Gymgather

class GUI(Frame):
    def button1Press():
        print("Start Workout")
        gym = Gymgather()
        gym.start_workout()

    def button2Press():
        print("How to use")
        tempWindow = Tk()
        tempWindow.geometry("600x300+650+400")
        tempWindow.title("How to use")
        tempWindow.configure(background = '#25274D')
        displayText = Text(tempWindow, height = 10, width = 40, font = ('Calibri', 20), bg = '#25274D', fg = '#AAABB8', bd = 0,)
        displayText.insert(INSERT, "1.) \"S\" is to snap shots during data collection ")
        displayText2 = Text(tempWindow, height = 10, width = 40, font = ('Calibri', 20), bg = '#25274D', fg = '#AAABB8', bd = 0,)
        displayText2.insert(INSERT, "2.) \"X\" is used to terminate the data collection.")
        displayText3 = Text(tempWindow, height = 10, width = 40, font = ('Calibri', 20), bg = '#25274D', fg = '#AAABB8', bd = 0,)
        displayText3.insert(INSERT, "3.) \"Q\" is used to quit the live feed for attendance")
        displayText.place(x = 17, y = 20)
        displayText2.place(x = 17, y = 60)
        displayText3.place(x = 17, y = 100)


    #def button3Press():
        # print("Start Attendance")
        #live_feed = Scan()
        #live_feed.start()

    window = Tk()
    window.title("Gymgather")

    btn1 = Button(window, text="Start work out", bg='#464866', activebackground = "#29648A", 
    width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button1Press, cursor = "cross")
    btn1.place(x =  410, y = 420)
    btn2 = Button(window, text = "How to use", bg='#464866', activebackground = "#29648A", 
    width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button2Press, cursor = "pirate")
    btn2.place( x = 410, y = 320)

    # btn3 = Button(window, text="Start Attendance", bg='#464866', activebackground = "#29648A", 
    # width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button3Press)
    # btn3.place( x = 410, y = 220)

        #btn3 = Button(window, text='blah blah', style= 'testStyle3', command=None).pack()
    #btn2.grid(row = 50, column = 100)
    #startText = Text(window, bg = "#AAABB8", font = ("Helvetica, 30"), text = "On Site")
    #startText.place( x = 410, y = 100)
    startText = Text(window, height = 1, width = 8, font = ('Calibri', 50), bg = '#25274D', fg = '#AAABB8', bd = 0, cursor = "heart")
    startText.insert(INSERT, "Gym")
    startText.insert(END, "Gather")
    startText['state'] = 'disabled'
    startText.place( x = 395, y = 100)
    
    #startText.pack()
    window.geometry("1024x526+250+130")
    window.configure(background = '#25274D')
    window.mainloop()
    #25274D