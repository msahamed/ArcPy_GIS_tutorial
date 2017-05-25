
# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Explanation of this file : www.youtube.com/user/sabberfoundation

import arcpy

fields = arcpy.ListFields("C:\GISLectures\Lectures\Cursor\Gravity.shp")


for fld in fields :
     print fld.name, fld.type


