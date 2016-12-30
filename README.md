

# tempChange
Program for automatically changing the temperature of a Gcode file at a given height increments
Tested in python 3.

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
