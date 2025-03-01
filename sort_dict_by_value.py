# Sample dictionary
dic = {
    "apple": 5,
    "banana": 2,
    "cherry": 7,
    "date": 3
}

# Sorting the dictionary by its values
sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1]))

print("Original dictionary:", dic)
print("Dictionary sorted by values:", sorted_dic)
