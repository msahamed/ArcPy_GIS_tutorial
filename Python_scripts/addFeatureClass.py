# Sabber Ahamed
# Graduate Research Assistant
# Center for Eartqhauke Research and Information
# The University of Memphis
# Memphis TN, USA

# Explanation of this file : www.youtube.com/user/sabberfoundation


# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "C:/Users/owner/Desktop/Lectures"
referenceData = "C:/Users/owner/Desktop/Lectures/Cursor/Gravity.shp"

# Set local variables
out_path = "C:/Users/owner/Desktop/Lectures"
out_name = "houses.shp"
geometry_type = "POINT"
template = "study_quads.shp"
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_reference = arcpy.Describe("C:/Users/owner/Desktop/Lectures/Cursor/Gravity.shp").spatialReference
# spatial_reference = arcpy.SpatialReference(32145)
# spatial_reference = arcpy.SpatialReference("c:/coordsystems/NAD 1983.prj")
# spatial_reference = arcpy.SpatialReference("Hawaii Albers Equal Area Conic")


# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)