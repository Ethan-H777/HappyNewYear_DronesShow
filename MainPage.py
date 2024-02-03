from tkinter import *
from tkinter import ttk
from locations import locations_dict


def on_depart_loc_selected(event=None):
	# Update the coordinate section when there is a change in location
    selected_location = depart_loc.get()
    selected_location = selected_location.replace("'", "").replace(",", "")
	
    location_coord_lat = locations_dict[selected_location]["lat"]
    location_coord_lng = locations_dict[selected_location]["lng"]

    x_entry_des.delete(0, 'end') 
    x_entry_des.insert(0, location_coord_lat)  
   
    y_entry_des.delete(0, 'end')  
    y_entry_des.insert(0, location_coord_lng)  
	
class MainPage(Frame):
	# Save all config changes to the json file
	def update_config(self):
		# Save all config changes to the json file
		self.controller.update_config("depart_loc", depart_loc.get())
		self.controller.update_config("x_coord_des", x_entry_des.get())
		self.controller.update_config("y_coord_des", y_entry_des.get())
		self.controller.update_config("distance", dist_entry.get())
		self.controller.update_config("colour", str(colour_var.get()))
		self.controller.update_config("colour", str(colour_var.get()))
		self.controller.get_config()

	# The second page of the application -  Here we will have a bunch of inputs for the drone show such as the starting/ending locations
	def __init__(self, parent, controller):

		# Slylistic variables
		heading_font = ("Helvetica", 20, "bold")
		heading_padX = 10
		heading_padY = 10
		label_font = ("Helvetica", 18)

		# Global varibles which are the entry that store user inputs
		global depart_loc
		global x_entry_des
		global y_entry_des
		global dist_entry
		global colour_var
		
		Frame.__init__(self, parent)
		self.controller = controller

		# Create a canvas and set its background to dark purple
		self.configure(background="#5941A9")

		# Display informational text for this page
		# label = Label(self, text="This is page 2. Here we will put all of the info regarding the flight plan.")
		# label.pack(side="top", fill="x", pady=10)

		"""DEPARTURE DATA"""
		# Create a container frame for the departure information
		departure_container = Frame(self, bg="#BEB8EB")
		departure_container.pack(side="top", fill="both", expand=True, padx=5, pady=5)

		# Departure label
		departure = Label(departure_container, text="Departure", bg="#BEB8EB", font=heading_font)
		departure.pack(side="top", anchor="w", padx=heading_padX, pady=heading_padY)

		# Create and configure the combobox
		depart_loc = ttk.Combobox(departure_container, values=list(locations_dict.keys()))
		depart_loc.pack(side="top", anchor="w", padx=heading_padX, pady=0)
		depart_loc.bind("<<ComboboxSelected>>", on_depart_loc_selected)

		"""DESTINATION DATA"""
		# Create a container frame for the destination information
		destination_container = Frame(self, bg="#BEB8EB")
		destination_container.pack(side="top", fill="both", expand=True, padx=5, pady=5)

		# Destination label
		destination = Label(destination_container, text="Destination", bg="#BEB8EB", font=heading_font)
		destination.pack(side="top", anchor="w", padx=heading_padX, pady=heading_padY)

		# Container for x-coordinate widgets (contain text label and entry box)
		x_coord_container_des = Frame(destination_container, bg="#BEB8EB")
		x_coord_container_des.pack(side="top", anchor="w", padx=15, pady=2)

		# Text label for x coordinate
		x_coord_des = Label(x_coord_container_des, text="Latitude   ", bg="#BEB8EB", font=label_font)
		x_coord_des.pack(side="left", anchor="w", padx=2, pady=2)

		# Text box for x coordinate
		x_entry_des = Entry(x_coord_container_des)
		x_entry_des.insert(0, 0)  # Set the default value
		x_entry_des.pack(side="left", padx=2, pady=2)

		# Container for y-coordinate widgets (contain text label and entry box)
		y_coord_container_des = Frame(destination_container, bg="#BEB8EB")
		y_coord_container_des.pack(side="top", anchor="w", padx=15, pady=5)

		# Text label for y coordinate
		y_coord_des = Label(y_coord_container_des, text="Longitude", bg="#BEB8EB", font=label_font)
		y_coord_des.pack(side="left", anchor="w", padx=2, pady=2)
		
		# Text box for y coordinate
		y_entry_des = Entry(y_coord_container_des)
		y_entry_des.insert(0, 0)  # Set the default value
		y_entry_des.pack(side="left", padx=2, pady=2)


		"""ADVANCED SETTING"""
		# Create a container frame for the advanced settings
		adv_setting_container = Frame(self, bg="#BEB8EB")
		adv_setting_container.pack(side="top", fill="both", expand=True, padx=5, pady=5)

		# Label for Advance Settins (optional)
		adv_label = Label(adv_setting_container, text="Advanced Settings (optional)", bg="#BEB8EB", font=heading_font)
		adv_label.pack(side="top", anchor="w", padx=heading_padX, pady=heading_padY)

		# Container distance between drones widgets (contain text label and entry box)
		dist_container = Frame(adv_setting_container, bg="#BEB8EB")
		dist_container.pack(side="top", anchor="w", padx=15, pady=2)

		# Text label for distance between drones
		dist_label = Label(dist_container, text="Distance between drones (in metres)", bg="#BEB8EB", font=label_font)
		dist_label.pack(side="left", anchor="w", padx=2, pady=2)

		# Entry for distance between drones
		dist_entry = Entry(dist_container)
		dist_entry.insert(0, 1)
		dist_entry.pack(side="left", padx=2, pady=2)

		# Container colours widgets (contain 1 label and 2 radio buttons)
		colour_container = Frame(adv_setting_container, bg="#BEB8EB")
		colour_container.pack(side="top", anchor="w", padx=15, pady=2)
		
		# Text label for Colour
		colour_label = Label(colour_container, text="Colour:", bg="#BEB8EB", font=label_font)
		colour_label.pack(side="left", anchor="w", padx=(2, 15), pady=5)

		# Value for colour (Yes or No), default is No
		colour_var = StringVar()
		colour_var.set("0")

		# Yes to colour simulation
		yes_radio = Radiobutton(colour_container, text="Yes", variable=colour_var, value="1", bg="#BEB8EB", font=label_font)
		yes_radio.pack(side="left")

		# No to colour simulation
		no_radio = Radiobutton(colour_container, text="No", variable=colour_var, value="0", bg="#BEB8EB", font=label_font)
		no_radio.pack(side="left")


		"""BUTTONS"""
		buttons_container = Frame(self, bg="#5941A9")
		buttons_container.pack(side="bottom", pady=2)

		# Create a button to navigate back to the start page
		back_button = Button(buttons_container, text="Back", command=lambda: controller.show_frame("LandingScreen"))
		back_button.pack(side="left", padx=(0, 250), pady=10)

		# Create a next button
		next_button = Button(buttons_container, text='Next', command= lambda: [self.update_config(), controller.show_frame("FilePage")])
		next_button.pack(side="left", anchor="e", padx=10, pady=10)


