first_list = eval(input("Enter the first list: "))
second_list = eval(input("Enter the second list: "))

common_elements = []

for element in first_list:
    if element in second_list:
        common_elements.append(element)

print("Common elements: ", common_elements)