import json
import xmltodict

json_loc = r'/home/adam/repos/testing_area/good_tanker (copy).json'

# Read the JSON file
with open(json_loc, "r") as f:
    json_data = json.load(f)

# Convert the JSON data to an XML string
xml_data = xmltodict.unparse(json_data)

# Write the XML string to an XML file
with open("data.xml", "w") as f:
    f.write(xml_data)