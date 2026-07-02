def find_max(lst):
    max_value = lst[0]  # Initializing a storage for the max_value
    # TODO: traverse the list. If an element is greater than max_value, assign max_value to this element
    max_value = max(lst)
    return max_value

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Calling the find_max function
    max_value = find_max(numbers)

    print("The maximum value is:", max_value)  # The maximum value is: 5