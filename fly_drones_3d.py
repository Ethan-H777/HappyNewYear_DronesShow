# python fly_drones.py <json filename> <drones_num>
# e.g. python fly_drones.py 3d-6coords.json 6

import time
import threading
from dronekit import connect, VehicleMode, LocationGlobalRelative
import sys
import numpy as np
sys.path.append("GeoCoordinateGeneration")
from coord_conversion_function import main

# To improve this script, we will automate the coordinate generation, add multiple confiurations to the show etc

def start_drone(connection_string, target_locations):
    print("Connecting to the drone through port", connection_string, " and sending to location @ ", target_locations)
    
    # Connecting the the drones mavlink
    vehicle = setup_drone(connection_string)

    control_drone(vehicle, connection_string, target_locations)

    # Once the vehicle has been at location for 2 miniutes, return to the landing site.
    return_to_launch(vehicle)

    print(f"{connection_string}: All drones are returning... script has been completed")

def control_drone(vehicle, connection_string, target_locations):

    # Attempt to change the vehicle mode to GUIDED and arm vehicle
    vehicle.mode = VehicleMode("GUIDED")

    # Check every second if the mode change has been successful
    while not vehicle.mode.name == "GUIDED":
        time.sleep(1)

    while not vehicle.is_armable:
        print(f"{connection_string}: Waiting for drone.. Currently not armable...")
        time.sleep(1)

    # Drone is armable, all systems are nominal
    vehicle.armed = True

    while not vehicle.armed:
        print(f"{connection_string}: Drone is armable, but still awaiting confirmation of armed drone...")
        time.sleep(1)

    # Takeoff is initiated for an altitude of 10m
    vehicle.simple_takeoff(10)

    # While loop to make drone fly to 95% of the takeoff altitude target, then goto the first show
    while True:
        if check_reach_target_altitude(vehicle) == True:
                break
        time.sleep(1)


    # Adding the target location to the drones mission.
    go_to_target_locations(vehicle, target_locations, connection_string)

    # time.sleep(20)
    time.sleep(10)

def setup_drone(connection_string):
    return connect(connection_string, wait_ready=False)

def check_reach_target_altitude(vehicle):
        altitude = vehicle.location.global_relative_frame.alt
        print(f" Altitude: {altitude}")
        if altitude >= 10 * 0.95:  # Trigger when 95% of the desired altitude is reached
            print("Reached target altitude")
            return True
        
def go_to_target_locations(vehicle, target_locations, connection_string):
    for target_location in target_locations:
        print(f"{connection_string}: Going to new location in the show..", target_location)
        vehicle.simple_goto(target_location)
        time.sleep(100)

def return_to_launch(vehicle):
    vehicle.mode = VehicleMode("RTL")
    time.sleep(100)


def run(x_centre, y_centre, formation_directory, m_seperation):
    # Different target locations (latitude, longitude, altitude) --> currently hardcoded.
    locations, drones_num = main(x_centre, y_centre, formation_directory, m_seperation)

    # Connection strings for all drones in the show at the moment
    connection_strings = [f"127.0.0.1:{port}" for port in range(8101, 8101+drones_num*100, 100)]
    print("The connection strings for this show include:", connection_strings)

    # Creating a thread for each drone, then adding them to this list
    threads = []
    for conn_str, loc in zip(connection_strings, locations):
        # Create one thread per drone
        thread = threading.Thread(target=start_drone, args=(conn_str, loc))
        thread.start()
        # Once started, add the thread to join them later
        threads.append(thread)

    for t in threads:
        print("Drone thread has finished", t)
        t.join()

    print("All drones have completed their missions.")

#run(-35.363262, 149.165237, "2D-15coords", 1000)
