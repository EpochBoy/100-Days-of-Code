programmin_dict = {
    "Test1": "Jeg er test1",
    "Test2": "Jeg er test2"
}


programmin_dict["Test3"] = "Test3 added"

print(programmin_dict)

#Empty dict
empty_dict = {}

#Edit dict
programmin_dict["Test2"] = "Test has changed"
print(programmin_dict)

#Loop through dict
for key in programmin_dict:
    print(key+" "+programmin_dict[key])

#Wipe existing
programmin_dict = {}

print(f"Content of program dict {programmin_dict}")

#Nesting list and dicts
print("NESTING LISTS AND DICTS BELOW THIS LINE")
print("=======================================")

capitals = {
    "France": "Paris",
    "Denmark": "Copenhagen",
}

#Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lile", "Nancy"],
    "Denmark": ["Copenhagen", "Odense", "Skanderborg"]
}

#Nesting a dictionary in a dictionary
travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lile", "Nancy"],
        "total_visits": 12
        },
    "Denmark":{
        "cities_visited": ["Copenhagen", "Odense", "Skanderborg"],
        "total_visits": 12
        }
}

#Nesting a Dictionary inside a list

travel_log3 = [
    {
    "country": "France", 
    "cities_visited": ["Paris", "Lile", "Nancy"],
    "total_visits": 12
    },
    {
    "country": "Denmark",
    "cities_visited": ["Copenhagen", "Odense", "Skanderborg"],
    "total_visits": 12
    }
]

print(travel_log3)