# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Purpose of this code : To teach how to see all the Fields of aFeature class
# Explanation of this file : www.youtube.com/user/sabberfoundation


import arcpy

# Create a Describe object from the feature class
#
desc = arcpy.Describe("C:\GISLectures\Lectures\Cursor\Gravity.shp")



# Print some feature class properties
#
print "Feature Type:  " + desc.featureType
print "Shape Type :   " + desc.shapeType
print "Spatial Index: " + str(desc.hasSpatialIndex)
print "Has M Value:  " +   str(desc.hasM)
print "Has Z Value:  " +    str(desc.hasM)
print "Shape field name : " + str(desc.ShapeFieldName)

# Spatial reference :

sr = desc.SpatialReference
print "spatial reference type : " + str(sr.Type)