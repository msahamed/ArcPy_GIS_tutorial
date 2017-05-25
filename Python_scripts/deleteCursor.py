# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Explanation of this file : www.youtube.com/user/sabberfoundation

import arcpy

# feature class
fc = "C:\GISLectures\Lectures\Cursor\Gravity.shp"

# get cursor object to delete a row
cursor = arcpy.UpdateCursor(fc)

for row in cursor :
	# check if a row has LENGTH value = 10 and 
	# B_GRAVG_ vale has 3
	if row.LENGTH == 10 and row.B_GRAVG_ == 3:

		# if satisfied above condition its gonna delete row
		cursor.deleteRow(row)

# delete cursor to free memory
del cursor


