
# Tunction sum_list that takes a list of integers as an argument and returns the sum of its elements
def sum_list(lst):
    if not lst:
        return 0
        
    total_sum = lst[0]
    print("Initial sum: ", total_sum)
    
    # Slicing from index 1 onward to avoid adding the first element twice
    for item in lst[1:]:
        # Adding the individual item
        total_sum += item
    return total_sum

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Sum of list:", sum_list(numbers))  # Output: Sum of list: 15