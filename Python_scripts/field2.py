
# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Purpose of this code : To teach how to see all the Fields of aFeature class
# Explanation of this file : www.youtube.com/user/sabberfoundation


import arcpy

feature_class = "C:\Users\owner\Desktop\Lectures\Cursor\gravpointsfff.shp"

# Create a list of fields using the ListFields function
fields = arcpy.ListFields(feature_class)

# Iterate through the list of fields
for field in fields:
    # Print field properties
    print("Field:       {0}".format(field.name))
    print("Alias:       {0}".format(field.aliasName))
    print("Type:        {0}".format(field.type))
    print("Is Editable: {0}".format(field.editable))
    print("Required:    {0}".format(field.required))
    print("Scale:       {0}".format(field.scale))
    print("Precision:   {0}".format(field.precision))
    # print("Field: {0}, Alias: {1}, Type: {2} ".format(field.name, field.aliasName, field.type))