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

arcpy.DeleteField_management(fc, ["second", "third", "Physics", "Chemistry"])