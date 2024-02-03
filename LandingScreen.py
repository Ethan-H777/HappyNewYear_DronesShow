from tkinter import *
from PIL import ImageTk, Image
import sys
import os

class LandingScreen(Frame):
    #The main start page of the application - Here we will have a simple button and the AeroGlow logo

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Create a canvas and set its background to white
        canvas = Canvas(self, width=600, height=400)
        canvas.configure(background='white')
        canvas.pack()

        # Display welcome text on the canvas
        welcome_text = "AeroGlow!"
        canvas.create_text(300, 200, text=welcome_text, font=("Arial", 32), fill="black")

        # Check if EXE and executre accordingly
        if getattr(sys, 'frozen', False):
            base_img_path = sys._MEIPASS
        else:
            base_img_path = os.path.dirname(__file__)

        image_path = os.path.join(base_img_path, "Images/logo2.jpg")

        global file_img

        img = Image.open(image_path)
        img = img.resize((585, 470))
        file_img = ImageTk.PhotoImage(img)
        
        # Insert the image as an label without packing
        img_label = Label(canvas, image=file_img)
        img_label.pack(anchor=CENTER)

        # Create a button to navigate to the next page
        button = Button(self, text="Next", command=lambda: controller.show_frame("MainPage"))
        button.pack(pady=20)
