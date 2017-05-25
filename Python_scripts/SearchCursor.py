import arcpy

feature_class = "c:/data/counties.shp"

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