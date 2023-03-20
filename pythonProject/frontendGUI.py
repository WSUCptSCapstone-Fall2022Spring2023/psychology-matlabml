"""
This file contains the frontend for the application.
It interfaces with the API Frontend to Local Backend to communicate with the rest of the application's backend.
This app does not interface with the backend yet.
"""

from tkinter import *  # import tkinter


def choose_folder():
    """Method that opens a file explorer window to select a folder to read"""
    try:
        import tkinter
    except ImportError:
        print("Tkinter not installed.")
        exit()

    from tkinter import filedialog

    # Suppress the Tkinter root window
    #tkroot = tkinter.Tk()
    #tkroot.withdraw()

    return str(tkinter.filedialog.askdirectory())



if __name__ == "__main__":

    print()







