import json
import math
from geopy.distance import geodesic
from dronekit import LocationGlobalRelative
import os
from xml.dom.minidom import Document
from datetime import datetime
import random
import string
import csv

#Retreive data from csv files and convert them into vectors
def get_data(directory_path):
    all_file_contents = []
    num_drones = 0
    for filename in os.listdir(directory_path):
        f = os.path.join(directory_path, filename)

        # checking if it is a file
        if os.path.isfile(f):
            num_drones += 1
            single_file_contents = []
            with open(f, 'r') as file:
                csvreader = csv.reader(file, delimiter=',')
                next(file)
                for row in csvreader:
                    vectors = [float(row[1]), float(row[2]), float(row[3])]
                    single_file_contents.append(vectors)
            
            all_file_contents.append(single_file_contents)
    return all_file_contents, num_drones

#Find euclidian distance from the centre
#! fix it not including z coordinates?
def calculate_distance_from_origin(x, y, z=0):
    return math.sqrt(x**2 + y**2 + z**2)

#Calculate geocoordinate from centre using distance and azimuth
def calculate_new_geo_coordinate(lat, lon, azimuth, distance):
    start = (lat, lon)
    d = geodesic(kilometers=distance).destination(start, azimuth)
    return d.latitude, d.longitude #, d.altitute -> update for 3D when we need a variable height of drones

#Find all azimuths
def find_azimuths(vectors):
    azimuths = []
    for x, y, _ in vectors:
        radian_azimuth = math.atan2(y, x)
        degree_azimuth = (radian_azimuth * 180 / math.pi) % 360
        azimuths.append(degree_azimuth)
    
    return azimuths

def main(ref_lat, ref_lon, blender_directory, m_seperation):
    data, num_drones = get_data(blender_directory)

    geocoord_array = []

    for drone_array in data:
        azimuths = find_azimuths(drone_array)

        altitude = [z for _,_,z in drone_array]

        #Find adjusted distances from centre
        distances = [calculate_distance_from_origin(x, y) for x, y, _ in drone_array]
        adjusted_distances = [d * m_seperation for d in distances]
        geo_coordinates_adjusted = []

        #Find geo coordinate from azimuths and distances
        for i, azimuth in enumerate(azimuths):
            distance_kilometers = adjusted_distances[i] / 1000
            lat_new, lon_new = calculate_new_geo_coordinate(ref_lat, ref_lon, azimuth, distance_kilometers)
            geo_coordinates_adjusted.append(LocationGlobalRelative(lat_new, lon_new, altitude[i])) #update for 3D when we need a variable height of drones

        geocoord_array.append(geo_coordinates_adjusted)
    
    return geocoord_array, num_drones

#print(main(0, 0,"3D-6coords", 1000))
#get_data("2D-15coords")