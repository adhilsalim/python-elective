# get elements for the dictionary from the user

DictOne = {}

# get the number of elements for the dictionary
num_of_elements = int(input("Enter the number of elements for the dictionary: "))

# get the elements for the dictionary from the user
for i in range(num_of_elements):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    DictOne[key] = value

# display the dictionary
print("\nDictionary:", DictOne)

# create a new dictionary with the opposite mapping
DictTwo = {}

# get the opposite mapping for the dictionary
for key in DictOne:
    value = DictOne[key]
    DictTwo[value] = key


# display the dictionary with the opposite mapping
print("\nDictionary with the opposite mapping:", DictTwo)