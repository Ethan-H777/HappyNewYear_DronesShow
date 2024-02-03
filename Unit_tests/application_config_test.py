import unittest
import json
from application import AeroGlowApplication

class TestApplicationConfig(unittest.TestCase):

    def test_initialise_config_file(self):
        # Create an instance of AeroGlowApplication
        app = AeroGlowApplication()

        # Call the initialise_config_file method
        app.initialise_config_file()

        expected_config = {"depart_loc" : "Null",
	                "x_coord_des" : "0",
                    "y_coord_des" : "0",
                    "distance" : "0",
                    "colour" : "0",
                    "directory_path" : "Null",
                    "export_format" : "0"}

        # Verify that the file was created and contains the expected configuration
        with open(app.file_path, "r") as json_file:
            actual_config = json.load(json_file)

        self.assertEqual(actual_config, expected_config)

    def test_get_config(self):
        app = AeroGlowApplication()
        app.initialise_config_file()

        expected_config = {"depart_loc" : "Null",
	                "x_coord_des" : "0",
                    "y_coord_des" : "0",
                    "distance" : "0",
                    "colour" : "0",
                    "directory_path" : "Null",
                    "export_format" : "0"}
        self.assertEqual(app.get_config(), expected_config)

    def test_update_config(self):
        app = AeroGlowApplication()
        app.initialise_config_file()

        app.update_config("depart_loc", "YourHouse")
        app.update_config("x_coord_des", "-1")
        app.update_config("y_coord_des", "1.5") 
        app.update_config("distance", "0.25")
        app.update_config("colour", "1")
        app.update_config("directory_path", "/home")
        app.update_config("export_format", "1")

        expected_config = {"depart_loc" : "YourHouse",
            "x_coord_des" : "-1",
            "y_coord_des" : "1.5",
            "distance" : "0.25",
            "colour" : "1",
            "directory_path" : "/home",
            "export_format" : "1"}
        
        self.assertEqual(app.get_config(), expected_config)
         
        

if __name__ == '__main__':
    unittest.main()
