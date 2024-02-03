import unittest
import math
from coord_conversion_function import *

class TestSum(unittest.TestCase):

    #Test if the distance is correctly calculated for a normal case of distances
    def test_distance_valid(self):
        result = calculate_distance_from_origin(1, 2, 3)
        self.assertEqual(result, math.sqrt(14))

    #Test if the distance is correctly calculated for an edge case of 0 distance
    def test_distance_0(self):
        result = calculate_distance_from_origin(0, 0, 0)
        self.assertEqual(result, 0)

    #Test if the geo coordinates are correctly calculated from vectors
    def test_geo_coordinates(self):
        result_lat, result_lon = calculate_new_geo_coordinate(30, 100, 45, 1000)
        self.assertEqual(result_lat, 36.14346316090063)
        self.assertEqual(result_lon, 107.84910560073311)

    
    #Test if the string vectors coordinates are correctly turned into tuples of numbers
    def test_get_data(self):
        data, ignore = get_data("test_directory")
        
        self.assertEqual(data, [[[-1.5, 0.0, 0.0], [-1.4943, 0.0, 0.071]], [[-1.5, -3.0, 0.0], [-1.5029, -3.0011, 0.0832]], [[-1.5, 0.0, 0.0], [-1.4943, 0.0, 0.071]], [[-1.5, -3.0, 0.0], [-1.5029, -3.0011, 0.0832]]])
    
    #Test if the azimuth can be found from tuples of vectors
    def test_find_azimuths(self):
        vectors = [(1, 1, 0.0000), (-1, 1, 0.0000)]
        azimuths = find_azimuths(vectors)
        
        self.assertEqual(azimuths, [45.0, 135.0])

    #Test an edge case with no vectors
    def test_find_azimuths_none(self):
        vectors = []
        azimuths = find_azimuths(vectors)
        
        self.assertEqual(azimuths, [])

if __name__ == '__main__':
    unittest.main()