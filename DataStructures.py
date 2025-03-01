String_1 = "Abhisghjghahaefhehek"
String = String_1.upper()
print(String)

mySet = set()

for i in range(len(String)):
    mySet.add(String[i])

print(mySet)

for i in mySet:
    print(i, end=", ")

print("\n")
# Iterating over the set without a space after the last element
print(" ".join(mySet))


print("LOGIC")
print("\n")
newStr = ""
for i in range(len(String)):
    if String[i] not in newStr:
        newStr += String[i]


print(newStr)


for i in range(1, 5):
    for j in range(i):
        print(j, end=" ")
