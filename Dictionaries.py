# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and does not allow duplicates.

dic = {
    "name": "Abhishek",
    "age": 21,
    "city": "Delhi",
    "Education": {"College": "IGNOU", "Course": "BCA"},
    "Hobbies": ["Coding", "Gaming", "Reading"]
}

dic1 = {
    "Gender" : "Male",
    "Occupation" : "Developer"  
}

# Adding a new key-value pair
dic1["Email"] = "Abhishek@gmail.com"
print(dic1)


# Accessing dictionary elements
print(dic)
print(dic.get("Education"))
print(dic.get("Hobbies"))
print(dic.get("Education").get("Course"))
print(dic.get("Hobbies")[1])

# Dictionary keys and values
print(dic.keys())
print(dic.values())



# Updating a value
dic["age"] = 22
print(dic)

# Removing a key-value pair
dic.pop("city")
print(dic)

# Iterating over keys and values
print("Iterating over keys and values ************************************************")
keyCount = 0 
for k , v in dic.items():
    keyCount += 1
    print(k ,v)
print("Number of keys in the dictionary: ", keyCount)

# Checking if a key exists
if "name" in dic:
    print("Name is present in the dictionary")

# merging two dictionaries
print("Merging two dictionaries ************************************************")
dic.update(dic1)
print(dic)


# Clearing all elements from the dictionaries
dic.clear()
dic1.clear()
print(dic)
print(dic1)