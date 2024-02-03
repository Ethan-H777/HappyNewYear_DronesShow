# Work with actual drones. 
# 1. Get the file with the blender infomation (what does this look like) -> A
# 2. Create 15 SITL, and manage their processes -> Sam
# 3. Run conversion software to get accurate flight plan for drone
# 4. Start flight of the drones
# 5. Communicate to front end the progress of the show. 


import subprocess
import time
import os

processes = []

def spawn_SITL(drone_number, location="SYD_TAKEOFF"):
    # Change directory to Tools/autotest
    path = os.path.expanduser("~/Desktop/ardupilot/Tools/autotest")
    os.chdir(path)

    # Initialize starting QGC and DroneKit ports
    start_qgc_port = 8100
    start_dronekit_port = 8101

    # Initialize the step size (spacing between each drone's ports)
    step_size = 100

    # Loop to launch 5 instances
    for i in range(1, drone_number + 1):
        # Calculate the QGC and DroneKit ports for this instance
        qgc_port = start_qgc_port + (i - 1) * step_size
        dronekit_port = start_dronekit_port + (i - 1) * step_size

        # Calculate instance number (0-based)
        inst = i - 1

        # Command to launch this instance in a new screen session
        cmd = [
            'screen', '-dmS', f"instance_{i}",
            './sim_vehicle.py', '-v', 'ArduCopter',
            '--sysid', str(i), f'-I{inst}', 
            f'--out=tcpin:0.0.0.0:{qgc_port}',
            f'--out=0.0.0.0:{dronekit_port}', '-L', location
        ]


        proc = subprocess.Popen(cmd)
        processes.append(proc)

        print(" ".join(cmd))

def terminate_SITL():
    global processes
    for proc in processes:
        print("TERMINATING", proc)
        proc.terminate()
    subprocess.run(["killall", "screen"])


    # Uncomment below to kill processes (handy to keep while debugging)
    # pattern = "arducopter -S --model \+ --"
    # subprocess.run(['pkill', '-f', pattern])

    processes = []

# Casual testing
#spawn_SITL(15)
#time.sleep(200)
#terminate_SITL()

