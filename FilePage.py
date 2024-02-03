from tkinter import *
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
import sys
import os

import tkinter as tk
from tkinter import ttk

def update_config(self, directory_path):
    print(directory_path)
    self.controller.update_config("directory_path", directory_path)

def popupWarn(msg): 
    tk.messagebox.showwarning(title="Alert", message=msg)

def popupInfo(msg): 
    tk.messagebox.showinfo(title="Alert", message=msg)

# def popupmsg(msg):
#     label_font = ("Helvetica", 18)

#     popup = tk.Tk()
#     popup.wm_title("Alert")

#     label = ttk.Label(popup, text=msg, font=label_font)
#     label.pack(side="top", fill="x", pady=10)

#     B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
#     B1.pack()

#     popup.mainloop()
     
class FilePage(Frame):
#The file page of the app taks input of csv coordinates file

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Slylistic variables
        heading_font = ("Helvetica", 20, "bold")
        heading_padX = 10
        heading_padY = 10
        label_font = ("Helvetica", 18)

        # Create a canvas and set its background to dark purple
        self.configure(background="#5941A9")

        '''INPUT FILES'''
        # Create a container frame for the title 
        title_container = Frame(self, bg="#BEB8EB")
        title_container.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        title = Label(title_container, text="Submit Your File Directory", bg="#BEB8EB", font=heading_font)
        title.pack(side="top", anchor="w", padx=heading_padX, pady=heading_padY)

        # Check if EXE and executre accordingly
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        image_path = os.path.join(base_path, "Images/File2.png")

        global file_img

        img = Image.open(image_path)
        img = img.resize((590, 360))
        file_img = ImageTk.PhotoImage(img)

        # default boolean - file not submit
        global file_submit
        file_submit = False


        # Insert the image as an label without packing
        img_label = Label(title_container, image=file_img)


        # file dialog function
        def callback():
            directory_path = fd.askdirectory() # store absolute path to input file
            global file_submit

            if directory_path and directory_path != "/":
                # user select directory and update json config file
                update_config(self, directory_path) 
                # update boolean to true
                file_submit = True
                msg = "Blender files directory submitted!"
                popupInfo(msg)
            else:
                file_submit = False
                # user didn't select any directory
                msg = "Directory missing!"
                popupWarn(msg)
            

        # Create a button using image instead of text
        file_button = Button(title_container, image=file_img, borderwidth=0, command=callback)
        file_button.pack(anchor="center")

        '''BUTTONS'''
        buttons_container = Frame(self, bg="#5941A9")
        buttons_container.pack(side="bottom", pady=2)
        
        # Create a button to navigate back to the main page
        back_button = Button(buttons_container, text="Back",borderwidth=0 , command=lambda: controller.show_frame("MainPage"))
        back_button.pack(side="left", padx=(0, 250), pady=10)

        # Create a next button
        next_button = Button(buttons_container, text='Next', borderwidth=0, command=lambda: nextExportPage())
        next_button.pack(side="left", anchor="e", padx=10, pady=10)
        
        # next button function, if file submit then change page, otherwise not.
        def nextExportPage():
            global file_submit
            if file_submit:
                controller.show_frame("ExportPage")
            else:
                msg = "Directory missing!"
                popupWarn(msg)
