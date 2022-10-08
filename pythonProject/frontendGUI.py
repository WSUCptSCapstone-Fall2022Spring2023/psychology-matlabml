"""
This file contains the frontend for the application.
It interfaces with the API Frontend to Local Backend to communicate with the rest of the application's backend.
Currently, running this file opens a small window with a button that displays a message when pushed.
This has no relevance to the project and is simply for learning tkinter.
"""

from tkinter import *  # import tkinter

# import API_Frontend_to_Local_Backend

main = Tk()  # creates the main window for the GUI


# function that is run whenever the button is clicked
def button_one_clicked():
    text = Label(main, text="you clicked the button!")  # create label widget
    text.pack()


text = "push the button"
text_Label = Label(main, text=text)  # creates label widget
text_Label.pack()  # packes label widget

button_one = Button(main, text="new button", fg="blue", command=button_one_clicked)  # creates a button widget
button_one.pack()  # uses the pack method to put the button in the GUI

main.mainloop()  # Creates the loop
