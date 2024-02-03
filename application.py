'''
AEROGLOW APPLICATION
This is the AeroGlow application. Here users will be able to upload their CSV file 
from blender and this will manage the SITL spawning and management. 

Things to note: 
- Right now, it is one file, but think it will be best practice to increase the number of files (ie one per page)
- To run, use python3 application.py    -> this will launch a tkinter window. 
'''

from tkinter import *
from LandingScreen import LandingScreen
from MainPage import MainPage
from FilePage import FilePage
from ExportPage import ExportPage
import json

class AeroGlowApplication(Tk):
    # Initialize the configration json file with a dictionary
    def initialise_config_file(self):
        config = {"depart_loc" : "Null",
	                "x_coord_des" : "0",
                    "y_coord_des" : "0",
                    "distance" : "0",
                    "colour" : "0",
                    "directory_path" : "Null",
                    "export_format" : "0"}

        with open(self.file_path, "w") as json_file:
            json.dump(config, json_file)

    def __init__(self, *args, **kwargs):
        # Initialize the main window
        Tk.__init__(self, *args, **kwargs)

        # Initialize the configration json file with a dictionary
        self.file_path = "show_config.json"
        self.initialise_config_file()
        
        # Create a main container for the frames
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # Configure the grid to stretch content
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold all frames/pages
        self.frames = {}
        
        # Create and store each frame or page
        for F in (LandingScreen, MainPage, FilePage, ExportPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Display the initial frame
        self.show_frame("LandingScreen")

    def show_frame(self, page_name):
        '''Raise a frame to the top to show it'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    # Given the key and new value, update the config json file
    def update_config(self, key, value):
        # retreive current config from json file
        config = self.get_config()
        # update config dictionary with new value
        config[key] = value

        with open(self.file_path, "w") as json_file:
            # replace the json file with new dictionary
            json.dump(config, json_file)
    
    # retreive config dictionary from json file
    def get_config(self):
        with open(self.file_path, "r") as json_file:
            loaded_data = json.load(json_file)

        self.json_data = loaded_data
        return loaded_data

if __name__ == "__main__":
    # Create and run the application instance
    app = AeroGlowApplication()
    app.mainloop()