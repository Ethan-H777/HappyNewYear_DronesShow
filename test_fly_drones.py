import unittest 
from unittest.mock import MagicMock, patch
from fly_drones_3d import *


class TestFlyDrones(unittest.TestCase):
    #Setup the fake drone
    def setUp(self):
        self.mockVehicle = MagicMock()

    #Test if the drone is accepted at a given altitude
    def test_reach_target_altitude(self):
        self.mockVehicle.location.global_relative_frame.alt = 9.6
        result = check_reach_target_altitude(self.mockVehicle)
        self.assertTrue(result)

        self.mockVehicle.location.global_relative_frame.alt = 10
        result = check_reach_target_altitude(self.mockVehicle)
        self.assertTrue(result)

    #Test an edge case where the drone should not be accepted at a given altitude
    def test_fail_to_reach_target_altitude(self):
        self.mockVehicle.location.global_relative_frame.alt = 9.4
        result = check_reach_target_altitude(self.mockVehicle)
        self.assertFalse(result)

    #Test that control drone makes the drone armed and in "Guided" mode
    def test_control_drone(self):
        # Set up mock behavior
        self.mockVehicle.is_armable = True
        self.mockVehicle.armed = False

        self.mockVehicle.checkReachTargetAltitude = MagicMock(return_value=True)  # Simulate reaching target altitude
        locations, ignore = main(-33.855139, 151.218391, "./2D-new_coords", 100)
        locations = list(zip(*locations))

        self.mockVehicle.location.global_relative_frame.alt = 10
        control_drone(self.mockVehicle, "127.0.0.1:8101", locations[0])

        self.assertTrue(self.mockVehicle.armed)
        self.assertEqual(self.mockVehicle.mode.name, "GUIDED")

    #Test the return to launch
    def test_returnToLaunch(self):
        return_to_launch(self.mockVehicle)
        self.assertEqual(self.mockVehicle.mode.name, "RTL")

if __name__ == '__main__':
    unittest.main()