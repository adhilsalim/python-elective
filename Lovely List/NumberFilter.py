original_list = eval(input("Enter a list of numbers separated by commas: "))
filtered_list = []

threshold_value = int(input("Enter a number to filter the list: "))

for item in original_list:
  if item < threshold_value:
    filtered_list.append(item)

print("Filtered list:", filtered_list)
