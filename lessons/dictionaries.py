"""Demonstration of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]


# Initialize to an empty dictionary
schools = dict()


# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150


# Print a dictionary literal representation
print(schools)


# Access a value by its key aka "lookup"
print(f"UNC has {schools['UNC']} students.")


# Remove a key-value pair from a dictionary (use its key)
schools.pop("Duke")


# Test for existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools.")
else:
    print("No key 'Duke' in schools.")


# Update / Reassign a key-value pair
schools["UNC"] = 2000
schools["NCSU"] += 200

print(schools)


# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict

# Alternatively, initialize key-value pairs
# You can change the spacing to make it easier to read, it's just a style choice
schools = {
    "UNC": 19400, 
    "Duke": 6717, 
    "NCSU": 26150
}

print(schools)


# What happens when a key does not exist?
# print(schools["UNCC"])


# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")