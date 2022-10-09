"""
This file contains the frontend for the application.
It interfaces with the API Frontend to Local Backend to communicate with the rest of the application's backend.
This app does not interface with the backend yet.
"""

from tkinter import *  # import tkinter

main = Tk()  # creates the main window for the GUI
main.geometry('600x350')

# function that is run whenever the button is clicked
def button_one_clicked():
    text = Label(main, text="This Feature Coming Soon!")  # create label widget
    text.place(x=225, y=200)




homeButton = Button(main, text="Home", fg="blue", command=button_one_clicked)  # creates a button widget
homeButton.place(x=0, y=0)  # uses the pack method to put the button in the GUI

buildButton = Button(main, text="Build Model", fg="blue", command=button_one_clicked)  # creates a button widget
buildButton.place(x=42, y=0)  # uses the pack method to put the button in the GUI

testButton = Button(main, text="Test Model", fg="blue", command=button_one_clicked)  # creates a button widget
testButton.place(x=115, y=0)  # uses the pack method to put the button in the GUI

predictButton = Button(main, text="Test Model", fg="blue", command=button_one_clicked)  # creates a button widget
predictButton.place(x=181, y=0)  # uses the pack method to put the button in the GUI

main.mainloop()  # Creates the window loop
