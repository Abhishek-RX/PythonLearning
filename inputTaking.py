# Input taking from user

# Taking user input for dictionary values
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
college = input("Enter college: ")
course = input("Enter course: ")
hobbies = input("Enter hobbies (comma-separated): ").split(',')

# Creating a dictionary with the user inputs
user_info = {
    "name": name,
    "age": age,
    "city": city,
    "Education": {"College": college, "Course": course},
    "Hobbies": hobbies
}

# Sorting the dictionary by values (this will only work for comparable values)
# Note: Sorting a dictionary by values is not always meaningful, especially with nested dictionaries
sorted_user_info = dict(sorted(user_info.items(), key=lambda item: str(item[1])))

# Printing the dictionary
print("User Information Dictionary:", user_info)
print("Sorted User Information Dictionary:", sorted_user_info)

