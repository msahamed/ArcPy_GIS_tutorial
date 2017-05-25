
# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Explanation of this file : www.youtube.com/user/sabberfoundation




import arcpy

# Create a Describe object from the table.
#
desc = arcpy.Describe("C:\Users\owner\Desktop\Lectures\Cursor\Gravity.shp")

# Print the names and types of all the fields in the table

for field in desc.fields:

    print field.name + " = " + field.type
