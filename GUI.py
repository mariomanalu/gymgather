import tkinter as tk
#import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from Gymgather import Gymgather

global entry

class GUI(Frame):
    def button1Press():
        print("Start Workout")
        gym = Gymgather()
        gym.start_workout()

    def button2Press():
        print("Set Work Out Goals")
        tempWindow = Tk()
        tempWindow.geometry("600x300+650+400")
        tempWindow.title("Set Work Out Goals")
        tempWindow.configure(background = '#4D96FF')


        def display_text():
            string= entry.get()
            label1.configure(text=string)
            label2.configure(text=string)
            label3.configure(text=string)
            tempWindow.destroy()

        #Initialize a Label to display the User Input
        label1=Label(tempWindow, text="Dumbbell Bicep Curl", font=("Courier 22 bold"))
        label1.pack()
        
        #Create an Entry widget to accept User Input
        entry= Entry(tempWindow, width= 40)
        entry.focus_set()
        entry.pack()

         #Initialize a Label to display the User Input
        label2=Label(tempWindow, text="Kettlebell Curl", font=("Courier 22 bold"))
        label2.pack()

        #Create an Entry widget to accept User Input
        entry= Entry(tempWindow, width= 40)
        entry.focus_set()
        entry.pack()

        #Initialize a Label to display the User Input
        label3=Label(tempWindow, text="Reverse Curl", font=("Courier 22 bold"))
        label3.pack()

        #Create an Entry widget to accept User Input
        entry= Entry(tempWindow, width= 40)
        entry.focus_set()
        entry.pack()

        #Create a Button to validate Entry Widget
        ttk.Button(tempWindow, text= "Okay",width= 20, command= display_text).pack(pady=20)


    def button3Press():
        print("Add Friends")
        tempWindow = Tk()
        tempWindow.geometry("600x300+650+400")
        tempWindow.title("Set Work Out Goals")
        tempWindow.configure(background = '#4D96FF')

        def display_text():
            string= entry.get()
            label1.configure(text=string)
            label2.configure(text=string)
            tempWindow.destroy()

        #Initialize a Label to display the User Input
        label1=Label(tempWindow, text="Name", font=("Courier 22 bold"))
        label1.pack()
        
        #Create an Entry widget to accept User Input
        entry= Entry(tempWindow, width= 40)
        entry.focus_set()
        entry.pack()

         #Initialize a Label to display the User Input
        label2=Label(tempWindow, text="Phone Number", font=("Courier 22 bold"))
        label2.pack()

        #Create an Entry widget to accept User Input
        entry= Entry(tempWindow, width= 40)
        entry.focus_set()
        entry.pack()

        #Create a Button to validate Entry Widget
        ttk.Button(tempWindow, text= "Okay",width= 20, command= display_text).pack(pady=20)

        #Create a Button to add more friends
        ttk.Button(tempWindow, text= "Add more friends",width= 20, command= display_text).pack(pady=20)

    window = Tk()
    window.title("Gymgather")

    btn1 = Button(window, text="Set Work Out Goals", bg='#464866', activebackground = "#29648A", 
    width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button2Press, cursor = "cross")
    btn1.place(x =  410, y = 220)

    btn2 = Button(window, text="Add Friends", bg='#464866', activebackground = "#29648A", 
    width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button3Press, cursor = "cross")
    btn2.place(x =  410, y = 320)

    btn3 = Button(window, text="Start work out", bg='#464866', activebackground = "#29648A", 
    width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button1Press, cursor = "cross")
    btn3.place(x =  410, y = 420)


    # btn3 = Button(window, text="Start Attendance", bg='#464866', activebackground = "#29648A", 
    # width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button3Press)
    # btn3.place( x = 410, y = 220)

        #btn3 = Button(window, text='blah blah', style= 'testStyle3', command=None).pack()
    #btn2.grid(row = 50, column = 100)
    #startText = Text(window, bg = "#AAABB8", font = ("Helvetica, 30"), text = "On Site")
    #startText.place( x = 410, y = 100)
    startText = Text(window, height = 1, width = 8, font = ('Calibri', 80), bg = '#25274D', fg = "white", bd = 0, cursor = "heart")
    startText.insert(INSERT, "Gym")
    startText.insert(END, "gather")
    startText['state'] = 'disabled'
    startText.place( x = 380, y = 50)
    
    #startText.pack()
    window.geometry("1024x526+250+130")
    window.configure(background = '#FD5D5D')
    window.mainloop()
    #25274D