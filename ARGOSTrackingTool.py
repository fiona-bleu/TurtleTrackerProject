#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Fiona Bolte-Bradhurst (fbb7@duke.edu)
# Date:   Fall 2024
#--------------------------------------------------------------

#ask user for a date
user_date = input("Enter a date (M/D/YYYY): ")

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a string line by line
line_list = file_object.readlines()

#close the file
file_object.close()

#building dictionaries
date_dict = {}
location_dict = {}

#pretend we read one line of data from file
for lineString in line_list:
    #check if line is in data line
    if lineString[0] in ("#","U"):
        continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #filtering dictionary records
    if obs_lc in ("1","2","3"):
        #adding items to dictionaries
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)

#iniitalize key list
keys = []

#loop through items in date_dict 
for key, value in date_dict.items():
    if value == user_date:
        keys.append(key)

#loop through keys and report locations
for key in keys: 
    location = location_dict[key]
    lat = location[0]
    lng = location[1]
    print(f"On {user_date}, Sara the turtle was seen at {lat}d Lat, {lng}d Lng.")
