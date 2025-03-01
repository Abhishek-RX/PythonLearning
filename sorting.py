import random

lst = list()

for i in range(10):
    lst.append(random.randint(1, 100))

print("Original list ", lst)

# Bubble Sort
count = 0
steps = 0

for i in range(len(lst)):
    flag = False
    for j in range(len(lst) - 1 - i):

        steps += 1
        if lst[j] > lst[j + 1]:
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp
            count += 1
            flag = True
    if flag == False:
        break


print("After bubble sort ", lst)
print("Number of swaps ", count)
print("Number of steps ", steps)

# Selection Sort


for i in range(len(lst)):
    first = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[first]:
            first = j
    temp = lst[first]
    lst[first] = lst[i]
    lst[i] = temp


print("After selection sort ", lst)


