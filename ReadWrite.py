# You can use the open function with the mode 'w' to open a file for writing.
# If the file does not exist, it will be created.
# If the file exists, its contents will be overwritten.

with open("Demo.txt", "w")as file:
    file.write("Hello world!\n")
    file.write("I am testing Write function in python\n")
    
# You can use the open function with the mode 'r' to open a file for reading.
# If the file does not exist, this will cause an error.
# If the file exists, its contents will be read.

with open("Demo.txt" , "r") as file:
   # print(file.read())
    content = file.read()
    print(content)
    print(type(content))
    
# You can use the open function with the mode 'a' to open a file for appending.
# If the file does not exist, it will be created.
# If the file exists, new data will be appended to it.

with open ("Demo.txt", "a") as file :
    file.write("This is the appended text\n")
    
with open("Demo.txt", "r") as file:
    print(file.read())


# CSV files are used to store tabular data in plain text.
# The csv module allows you to read and write CSV files.
# You can use the csv.reader function to read the contents of a CSV file.
# You can use the csv.writer function to write data to a CSV file.

import csv 

with open ("DEMO.csv", "w",newline = "")as file:
    Writer = csv.writer(file)
    Writer.writerow(["Name","Age","City"])
    Writer.writerow(["Abhishek",21,"Delhi"])    
    Writer.writerow(["John",25,"New York"])
    Writer.writerow(["Jane",22,"San Francisco"])
    
with open ("DEMO.csv", "r")as file:
    reader = csv.reader(file)
    print(type(reader))
    print(reader)
    for r in reader:
        print(r)
    