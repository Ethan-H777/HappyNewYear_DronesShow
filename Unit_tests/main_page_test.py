import unittest
from unittest.mock import patch
from application import AeroGlowApplication
from MainPage import MainPage
from tkinter import *
from tkinter import ttk

class TestMainPage(unittest.TestCase):
	
	def setUp(self):
		self.app = AeroGlowApplication()
		self.app.initialise_config_file()
		container = Frame(self.app)
		self.main_page = MainPage(container, self.app)
		
	@patch('MainPage.depart_loc.get', return_value='SYD_TAKEOFF') # mock depart_loc.get()
	@patch('MainPage.x_entry_des.get', return_value='-33.856122') # mock x_entry_des.get()
	@patch('MainPage.y_entry_des.get', return_value='151.215492') # mock y_entry_des.get()
	@patch('MainPage.dist_entry.get', return_value='0.2') # mock dist_entry.get()
	@patch('MainPage.colour_var.get', return_value='1') # mock colour_var.get()
	def test_update_config(self, mock_depart_loc, mock_x_entry, mock_y_entry, mock_dist_entry, mock_colour_var):
		# Call the update_config method
		self.main_page.update_config()

		self.assertEqual(mock_depart_loc.call_count, 1)  # Ensure that depart_loc.get() was called
		self.assertEqual(mock_x_entry.call_count, 1)  # Ensure that x_entry_des.get() was called
		self.assertEqual(mock_y_entry.call_count, 1)  # Ensure that y_entry_des.get() was called
		self.assertEqual(mock_dist_entry.call_count, 1)  # Ensure that dist_entry.get() was called
		self.assertEqual(mock_colour_var.call_count, 1)  # Ensure that colour_var.get() was called

		expected_config = {"depart_loc" : "SYD_TAKEOFF",
			"x_coord_des" : "-33.856122",
			"y_coord_des" : "151.215492",
			"distance" : "0.2",
			"colour" : "1",
			"directory_path" : "Null",
			"export_format" : "0"}
		
		# assert that update_config() correctly update all values
		self.assertEqual(self.app.get_config(), expected_config)


		# Add other assertions as needed
# -33.856122, 151.215492

if __name__ == '__main__':
	unittest.main()
