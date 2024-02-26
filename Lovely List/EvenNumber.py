input_list = eval(input("Enter the list: "))

even_numbers = []

for num in input_list:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers: ", even_numbers)