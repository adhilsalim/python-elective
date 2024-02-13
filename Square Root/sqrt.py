number = float(input("Enter a positive number: "))

python_estimate = number ** (1/2)

algorithm_estimate = 1
while "%0.9f" % algorithm_estimate != "%0.9f" % python_estimate:
    algorithm_estimate = (algorithm_estimate + number / algorithm_estimate) / 2

print("Python's square root estimate: ", python_estimate)
print("Algorithm's square root estimate: ", algorithm_estimate)