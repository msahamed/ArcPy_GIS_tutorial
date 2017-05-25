# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Explanation of this file : www.youtube.com/user/sabberfoundation


# Name: AddField_Example2.py
# Description: Add a pair of new fields to a table
 
# Import system modules
import arcpy
import math as m
 
# Set environment settings
fc = "C:\GISLectures\Lectures\Cursor\Gravity.shp"

a = m.sin(10) + m.cos(25) + 3**2

expression = "a"

# add a field
arcpy.AddField_management(fc, "physics", "DOUBLE")

# Calculate anything to this field
arcpy.CalculateField_management(fc, "physics", expression, "PYTHON_9.3")