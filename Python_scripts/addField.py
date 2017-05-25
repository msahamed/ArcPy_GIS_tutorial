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
 
# Set environment settings
fc = "C:\GISLectures\Lectures\Cursor\Gravity.shp"
Field_name = ["first", "second", "third" , "Physics" , "Math", "Chemistry"]
Data_type = ["LONG", "DOUBLE", "TEXT", "SHORT", "DATE", "LONG"]

# Add field to a table
for i in range(len(Field_name)):
	arcpy.AddField_management(fc, Field_name[i], Data_type[i])

