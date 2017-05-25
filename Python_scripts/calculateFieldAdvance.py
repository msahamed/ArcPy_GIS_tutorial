# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Explanation of this file : www.youtube.com/user/sabberfoundation

 
# Import system modules
import arcpy
 
# Set environment settings
fc = "C:\GISLectures\Lectures\Cursor\Gravity.shp"

# Obtain cursor object
cursor = arcpy.UpdateCursor(fc)

# Write function 
def calculateField(field1, field2):
	if field1 <= 5000 :
		return field1 * field2
	elif field1 > 5000 and field1 < 6000:
		return  field1 / field2
	else:
		return 0.0


# Go through all rows in a table and do some operations
for row in cursor:
	field1 = row.LENGTH
	field2 = row.B_GRAVG_
	row.physics = calculateField(field1, field2)
	cursor.updateRow(row) 

# Delete cursor and row objects to remove locks on the data 
del row 
del cursor

# Create 25 new rows.
numberOfRow = 100

# Operations
for i in range(numberOfRow):

	# create a new row
    row = cursor.newRow()

    # Update row values
    row.LENGTH = 10.0
    row.B_GRAVG_ = 1
    row.physics = 12.0

    # Insert updated row value
    cursor.insertRow(row) 

# Delete cursor and row objects
del cursor, row
