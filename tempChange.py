#
# Directions:
#
# 1. Slice object with following settings:
#       Print Settings:
#           Layer & Perimeter > Layer height: user preference
#           Support material > Generate support material: unchecked (disabled)
#           Advanced > extrusion width: 0.5mm
#
#       Filament Settings:
#           Filament > Temperature > Extruder > First layer: set to a reasonable temperature to get the part to stick tot he base
#           Filament > Temperature > Extruder > other layers: set to the same as first layer
#
#       Printer Settings:
#           Extruder > Retraction > Lift Z: This can be enabled if you typically use it
#
# 2. Copy g-code file into the same folder as this program.
# 3. Enter filename (with .gcode extension) of the file that you just copied into the user inputs below.
#       The name is case sensitive.
# 4. Enter output file name (with .gcode extension) in user inputs below. This will be the file
#       with the temperature changes. If this name matches the input file name it WILL BE OVERWRITTEN.
# 5. Enter the temperature the test will end at (the highest temperature you want to test) in user inputs below.
# 6. Enter the temperature increment to increase the temp by in each section in user inputs below.
# 7. Enter the height in millimeters of each test section of the model. 
#

import string
import re
from decimal import getcontext, Decimal


#
# User Inputs:
#
inputFileName = 'temp_calibration_tower.gcode' #g-code file to read in
outputFileName = 'temp_calibration_tower_test.gcode' #file to write modified g-code to
ending_temp = 220 #highest temp to test in degress C.
min_temp = 202
temperature_increment = 2 #jump up this many degrees C each section.
test_section_height = 12 #height in mm of each section.


#
# Program Variables
#
getcontext().prec = 3
index = 0
decrements = 0
zHeightList = list() #list of previously checked Z heights
command_list = list()
z_move = ""

with open(inputFileName, 'r') as f: #open file in read and write mode
    for line in f:
        command_list.append(line) #create list of all gcode commands
        
command_list.reverse() #flip list (work from top of model down)

for line in command_list:
    line = line.strip() #remove newline characters
    
    if 'G1 Z' in line: #find all Z height change commands
        command = line.split(" ") #parse codes
        if(command[1]):
            z_move = command[1]
            z_move = re.sub('[^0123456789\.]', '', z_move)
            if((Decimal(z_move) not in zHeightList) and (Decimal(z_move)% test_section_height == 0)):
                if(ending_temp - (temperature_increment * decrements) > min_temp):
                    tmp = ending_temp - (temperature_increment * decrements)
                else:
                    tmp = min_temp
                tmp_s = str(tmp)
                command_list.insert(index, 'M104 S' + tmp_s + '; automatic layer temp change \n')
                decrements +=1
                print('Inserting temperature at height ' + line)
            zHeightList.append(Decimal(z_move)) #add height to list to check against
    index += 1

command_list.reverse()
newfile = open(outputFileName, 'w')
for item in command_list:
    newfile.write("%s" % item)
newfile.close()

print('File changes complete!')

