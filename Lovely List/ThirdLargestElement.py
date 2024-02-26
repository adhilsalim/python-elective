numbers = eval(input("Enter the list of numbers: "))

for _ in range(2):
    largest_number = max(numbers)
    numbers[numbers.index(largest_number)] = 0

third_largest_number = max(numbers)
print("Third largest element =", third_largest_number)