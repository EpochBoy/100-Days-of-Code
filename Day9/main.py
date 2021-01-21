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