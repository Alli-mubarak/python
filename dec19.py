# Dictionaries
locations = {
    "headquarters": "New York",
    "flagship": "Paris"
}
# print(type(locations))
locations_hq = locations["headquarters"]
# # print(locations_hq)
# for details in locations:
#     print(locations[details])

locations["headquarters"] = "Canada"
# print(locations)
locations["admin"] = "Starlett"
locations["controller"] = "John Reyes"
locations["mayor"] = "Atland"
locations["director"] = "Conour"
locations["sub-control"] = "Laos"
# print(locations)

# for details in locations:
#     print(details + " is " + locations[details])
has_mayor = "mayor" in locations
has_major = "major" in locations
# print(has_major)
# print(has_mayor)
remove_mayor = locations.pop("mayor")

# print(remove_mayor)
# print(locations)
if "major" in locations:
    remove_major = locations.pop("major")
else:
    print(locations)