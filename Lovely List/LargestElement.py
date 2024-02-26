def find_largest_element(list_1):
    largest = list_1[0]
    for i in range(1, len(list_1)):
        if largest < list_1[i]:
            largest = list_1[i]
    return largest

def find_smallest_element(list_1):
    smallest = list_1[0]
    for i in range(1, len(list_1)):
        if smallest > list_1[i]:
            smallest = list_1[i]
    return smallest

def main():
    list_1 = eval(input("Enter the list: "))
    while True:
        print("Menu:")
        print("1. Find largest element using built-in max() function")
        print("2. Find largest element using manual method")
        print("3. Find smallest element using built-in min() function")
        print("4. Find smallest element using manual method")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Largest element in", list_1, "=", max(list_1))
        elif choice == 2:
            print("(manual method) Largest element in", list_1, "=", find_largest_element(list_1))
        elif choice == 3:
            print("Smallest element in", list_1, "=", min(list_1))
        elif choice == 4:
            print("(manual method) Smallest element in", list_1, "=", find_smallest_element(list_1))
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()