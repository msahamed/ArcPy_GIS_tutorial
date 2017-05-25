# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Explanation of this file : www.youtube.com/user/sabberfoundation

import arcpy

# feature class
fc = "C:\GISLectures\Lectures\Cursor\Gravity.shp"

# get cursor object
cursor = arcpy.InsertCursor(fc)

# number of row
numberOfRows = 100

for i in range(numberOfRows):
	# create an empty row
	row = cursor.newRow()

	# update the specied rows
	row.LENGTH = 10
	row.B_GRAVG_ = 3
	row.physics = 3.1416

	# Insert iupdated rows to table
	cursor.insertRow(row)

# delete cursor and rows object to free memory
del cursor, row