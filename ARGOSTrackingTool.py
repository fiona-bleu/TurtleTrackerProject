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

    #adding items to dictionaries
    date_dict[record_id] = obs_date
    location_dict[record_id] = (obs_lat, obs_lon)

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
  