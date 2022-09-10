""" This script can be used for all message requirements including, Heartbeat,
Entrance and Exit Gates, Follow the Path, Wildlife Encounter, Scan the Code,
Detect and Dock, Find and Fling, UAV Replenishment, and UAV Search and Report. """

___authors___ = "Ahmad Abu-Aysha & Lucas Schuurmans-Stekhoven"
___email___ = "a.abuaysha@uq.net.au & l.schuurmansstekhoven@uq.edu.au"

from datetime import datetime as dt
import time as clock
import serial
from dronekit import connect, VehicleMode, Command, mavutil

try:
    serial_connection = serial.Serial('COM3', baudrate=57600)
except:
    print('Radio not connected')

""" Use a variable to set which message needs to be sent in main() """

def standard_heartbeat():
    """ Pulls in data required to generate a heartbeat message and publishes
    message at a frequency of 1Hz
    Message format is
    Heartbeat Example Message: $RXHRB,111221,161229,21.31198,N,157.88972,W,ROBOT,2,1*11

    where

    Message ID $RXHRB Protocol Header
    AEDT Date 111221 ddmmyy Use Australian Eastern Daylight Time (AEDT)
    AEDT Time 161229 hhmmss (24hr time format) Use Australian Eastern Daylight Time (AEDT)
    Latitude 21.31198 Decimal degrees Provides ~1.11m accuracy N/S indicator N N=north, S=South
    Longitude 157.88972 Decimal degrees Provides ~1.04m accuracy E/W indicator W E=east, W=west
    Team ID ROBOT Team ID5-character code assigned by Technical Director
    System Mode 2 Current mode of AMS 1=Remote Operated 2=Autonomous 3=Killed
    UAV Status 1 Current UAV Status 1=Stowed 2=Deployed 3=Faulted
    The ‘Stowed’ state used only when the UAV is secured to the USV.
    The ‘Deployed’ state is used whenever the UAV is not on board the USV.
    Tools
    Checksum 11 Bitwise XOR
    <CR><LF>
    End of message
    """

    # May need to use try, except method for extracting data for other messages.

    while True: # Can remove this for main program

        # fetch lat long from vehicle object
        try:
            lat = str(vehicle.location.global_frame.lat)
        except:
            lat = ''
        try:
            long = str(vehicle.location.global_frame.lon)
        except:
            long = ''
        try:
            S = 'Get data'
        except:
            S = ''
        try:
            E = 'Get data' 
        except:
            E = ''
        try:
            sys_mode = 'Get data'
        except:
            sys_mode = ''
        try:
            uav_state = 'Get data' 
        except:
            uav_state = ''
            
        
        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
                str(dt.now().time().minute),
                str(dt.now().time().second)])

        message_fields = {
        "message_id" : "$RXHRB", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "lat" : lat, 
        "N_S" : S,
        "long" : long,
        "E_W" : E,
        "team_id" : "MANTI", # Assigned by Tech Director (CHANGE TO CONSTANT?)
        "sys_mode" : sys_mode,#TODO fetch sys_mode from central computer?
        "uav_state" : uav_state,#TODO fetch uav_state from central computer?
        "checksum" : "*11\n\r"
        }
        message = []

        

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.


def eegates_heartbeat():

   
    while True: # Can remove this for main program
        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
            str(dt.now().time().minute),
            str(dt.now().time().second)])
        entr_gate = '1'
        exit_gate = '1'

        message_fields = {
        "message_id" : "$RXGAT", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "team_id" : "MANTI",# Assigned by Tech Director (CHANGE TO CONSTANT?)
        "entr_gate" : entr_gate,#TODO Should this value be fetched from somewhere?
        "exit_gate" : exit_gate,#TODO Should this value be fetched from somewhere?
        "checksum" : "*11\n\r"
        }
        message = []

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.

def follow_path_heartbeat():
   
    while True: # Can remove this for main program
    
        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
            str(dt.now().time().minute),
            str(dt.now().time().second)])
        finished = '1'

        message_fields = {
        "message_id" : "$RXPTH", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "team_id" : "MANTI",# Assigned by Tech Director (CHANGE TO CONSTANT?)
        "finished" : finished, # Use a global variable for this.
        "checksum" : "*11\n\r"
        }
        message = []

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.


def wild_life_heartbeat():
    
  
    while True: # Can remove this for main program

        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
            str(dt.now().time().minute),
            str(dt.now().time().second)])
            
        num_detected = 'Get data'
        wild1 = 'Get data'
        wild2 = 'Get data'
        wild3 = 'Get data'

        message_fields = {
        "message_id" : "$RXPTH", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "team_id" : "MANTI",# Assigned by Tech Director (CHANGE TO CONSTANT?)
        "num_detected": num_detected,
        "1st wildlife": wild1,
        "2nd wildlife": wild2,
        "3rd wildlife": wild3,
        "checksum" : "*11\n\r"
        }
        message = []

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.


def scancode_heartbeat():
    
    while True: # Can remove this for main program

        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
            str(dt.now().time().minute),
            str(dt.now().time().second)])
        light_pattern = 'RGB' # Colors identified from first to last, over time.
    

        message_fields = {
        "message_id" : "$RXCOD", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "team_id" : "MANTI",# Assigned by Tech Director (CHANGE TO CONSTANT?)
        "light_pattern" : light_pattern,
        "checksum" : "*11\n\r"
        }
        message = []

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.


def dd_heartbeat():
  
    while True: # Can remove this for main program

        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
            str(dt.now().time().minute),
            str(dt.now().time().second)])
        colour = 'R' # Colour of the docking bay being attempted.
        ams_status = '1' # 1 = Docking, 2 = Docking Complete

        message_fields = {
        "message_id" : "$RXDOK", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "team_id" : "MANTI",# Assigned by Tech Director (CHANGE TO CONSTANT?)
        "colour" : colour,
        "ams_status" : ams_status,
        "checksum" : "*11\n\r"
        }
        message = []

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.


def ff_heartbeat():
   
    while True: # Can remove this for main program

        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
            str(dt.now().time().minute),
            str(dt.now().time().second)])
        colour = 'R' # Colour of the shape on the face being detected
        ams_status = '1' # 1 = Scanning, 2 = Flinging

        message_fields = {
        "message_id" : "$RXFLG", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "team_id" : "MANTI",# Assigned by Tech Director (CHANGE TO CONSTANT?)
        "colour" : colour,
        "ams_status" : ams_status,
        "checksum" : "*11\n\r"
        }
        message = []

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.

def uav_r_heartbeat():
    
 
    while True: # Can remove this for main program

        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
            str(dt.now().time().minute),
            str(dt.now().time().second)])
        uav_status = '1' # 1 = Stowed, 2 = Deployed, 3 = Faulted
        # See RobotX handbook for definitions on above.
        item_status = '0' # 0 = Not picked up, 1 = Picked up, 2 = Delivered
        # See RobotX handbook for definitions on above.

        message_fields = {
        "message_id" : "$RXUAV", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "team_id" : "MANTI",# Assigned by Tech Director (CHANGE TO CONSTANT?)
        "uav_status" : uav_status,
        "item_status" : item_status,
        "checksum" : "*11\n\r"
        }
        message = []

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.

def uav_s_heartbeat():

   
    while True: # Can remove this for main program

        date = str(dt.now().date())
        time = "".join([str(dt.now().time().hour), 
            str(dt.now().time().minute),
            str(dt.now().time().second)])
        object1_report = 'R' # 'R' or 'N'
        object1_lat = '21.33' # Will need to extract this data use try, except
        N_S_indic1 = 'N' # North or South indicator of object1?
        object1_lon = '157.3' # Will need to extract this data use try, except
        E_W_indic1 = 'W' # East or West indicator of object1?
        object2_report = 'R' # 'R' or 'N'
        object2_lat = '21.33' # Will need to extract this data use try, except
        N_S_indic2 = 'N' # North or South indicator of object1?
        object2_lon = '157.3' # Will need to extract this data use try, except
        E_W_indic2 = 'W' # East or West indicator of object1?
        uav_status = '1' # 1 = Stowed, 2 = Deployed, 3 = Faulted
        
        message_fields = {
        "message_id" : "$RXSAR", # Static message id
        "aedt_date" : date,
        "aedt_time" : time,
        "object1_report" : object1_report,
        "N_S_indic1" : N_S_indic1,
        "object1_lon" : object1_lon,
        "E_W_indic1" : E_W_indic1,
        "object2_report" : object2_report, 
        "object2_lat" : object2_lat, 
        "N_S_indic2" : N_S_indic2, 
        "object2_lon" : object2_lon, 
        "E_W_indic2" : E_W_indic2,
        "team_id" : "MANTI",# Assigned by Tech Director (CHANGE TO CONSTANT?)
        "uav_status" : uav_status,
        "checksum" : "*11\n\r"
        }
        
        message = []

        # Generate the message
        for i in message_fields:
            message.append(message_fields[i])
        final_message = ','.join(message)
        serial_connection.write(final_message.encode())
        clock.sleep(1) # May want to use an interrupt or if statement checking time past in main program.


    
def main():
    
        
    """In main program when ever a task is started make sure to update message_type global variable"""

    """ CONNECTION_STRING = '/dev/ttyUSB0' """ 
    message_type = 0 #Global variable to be changed depending on what task the system is currently performing
    print('Initializing Heartbeat')

    # create an autopilot connection object
    try:
        vehicle = connect(CONNECTION_STRING, wait_ready=True, baud=57600)
    except:
        print("Unable to connect to vehicle")

    if message_type == 0:
        standard_heartbeat()
    elif message_type == 1:
        eegates_heartbeat()
    elif message_type == 2:
        follow_path_heartbeat()
    elif message_type == 3:
        wildlife_heartbeat()
    elif message_type == 4:
        scancode_heartbeat()
    elif message_type == 5:
        dd_heartbeat()
    elif message_type == 6:
        ff_heartbeat()
    elif message_type == 7:
        uav_r_heartbeat()
    elif message_type == 8:
        uav_s_heartbeat()
            
        
        

    
    
