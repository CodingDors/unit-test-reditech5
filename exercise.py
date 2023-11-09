def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

def sum_positive_numbers(numbers):
    return sum([n for n in numbers if n > 0])

def find_largest_string(strings):
    return max(strings, key=len, default='')

def count_occurrences(numbers):
    occurrences = {}
    for n in numbers:
        if n in occurrences:
            occurrences[n] += 1
        else:
            occurrences[n] = 1
    return occurrences

def driver():
    while True:
        print("Choose a function to test:")
        print("1. Filter even numbers from a list.")
        print("2. Sum positive numbers from a list.")
        print("3. Find the largest string from a list of strings.")
        print("4. Count occurrences of numbers in a list.")
        print("5. Exit.")
        
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            filered_number = (filter_even_numbers(numbers))
            print(filered_number)
        elif choice == "2":
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print(sum_positive_numbers(numbers))

        elif choice == "3":
            strings = input("Enter strings separated by commas: ").split(", ")
            print(find_largest_string(strings))

        elif choice == "4":
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print(count_occurrences(numbers))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    driver()
