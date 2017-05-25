# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Explanation of this file : www.youtube.com/user/sabberfoundation

import arcpy

# feature class
fc = "C:\GISLectures\Lectures\Cursor\Gravity.shp"


# Create the spatial reference object
spatial_ref = arcpy.Describe(fc).spatialReference
if spatial_ref.name == "Unknow" :
	print "Unknow spatial reference"
else :
	print spatial_ref.name
	print spatial_ref.falseEasting