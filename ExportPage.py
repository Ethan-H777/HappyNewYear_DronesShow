from tkinter import *
import subprocess
import time
import os
from logic import *
from fly_drones_3d import *
from coord_conversion_function import get_data
import json
from FilePage import popupInfo

     
class ExportPage(Frame):
#The export page of the app ask for output format: simulation or real drone

    # Save all config changes to the json file
    def update_config(self):
        self.controller.update_config("export_format", str(export_var.get()))
        self.controller.get_config()
    
    def start_backend(self):
        loaded_data = self.controller.get_config()
        print(loaded_data['export_format'])
        if loaded_data['export_format'] == "0":
            print("Starting SITL")
            
            ignore, num_drones = get_data(loaded_data['directory_path'])

            spawn_SITL(num_drones, loaded_data['depart_loc'])
            time.sleep(60)
            print("Starting mission")

            #Need to put the number of drones in, but this hasn't been addressed in the application
            run(loaded_data['x_coord_des'], loaded_data['y_coord_des'], loaded_data['directory_path'], float(loaded_data['distance']))
            time.sleep(2)
            terminate_SITL()
            
        else:
            print("Trying to connect to real drones")
            run(loaded_data['x_coord_des'], loaded_data['y_coord_des'], loaded_data['directory_path'], float(loaded_data['distance']))

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Slylistic variables
        heading_font = ("Helvetica", 20, "bold")
        heading_padX = 10
        heading_padY = 10
        label_font = ("Helvetica", 18)

        global export_var
        global user_choice

        # Create a canvas and set its background to dark purple
        self.configure(background="#5941A9")

        # Create a container frame for the title 
        title_container = Frame(self, bg="#BEB8EB")
        title_container.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        title = Label(title_container, text="Export Format", bg="#BEB8EB", font=heading_font)
        title.pack(side="top", anchor="w", padx=heading_padX, pady=heading_padY)

        # Export format widgets (contain 2 radio buttons)
        export_container = Frame(title_container, bg="#BEB8EB")
        export_container.pack(side="top", anchor="w", padx=15, pady=2)

        # Value for format options (Simulation or Real drone), default is Simulation
        export_var = StringVar()
        export_var.set("0")

        # Simulation
        sim_radio = Radiobutton(export_container, text="2D simulation", variable=export_var, value="0", bg="#BEB8EB", font=label_font)
        sim_radio.pack(side="left")

		# Real drones
        real_radio = Radiobutton(export_container, text="Real drones", variable=export_var, value="1", bg="#BEB8EB", font=label_font)
        real_radio.pack(side="left")

        '''BUTTONS'''
        buttons_container = Frame(self, bg="#5941A9")
        buttons_container.pack(side="bottom", pady=2)
        
        # Create a button to navigate back to the File page
        back_button = Button(buttons_container, text="Back",borderwidth=0 , command=lambda: controller.show_frame("FilePage"))
        back_button.pack(side="left", padx=10, pady=10)

        # Create a Start button, that runs the above run function
        next_button = Button(buttons_container, text='Start My Show!', borderwidth=0, command= lambda: [self.update_config(), self.start_backend()])
        next_button.pack(side="left", anchor="e", padx=10, pady=10)

        # Create a button to navigate back to the Main page and kill the show
        back_button = Button(buttons_container, text="End",borderwidth=0 , command=lambda: end_show())
        back_button.pack(side="left", padx=10, pady=10)

        def end_show():
            #check the show is started or not
            #to do: kill show
            popupInfo("Drones show killed.")
            controller.show_frame("MainPage")
 