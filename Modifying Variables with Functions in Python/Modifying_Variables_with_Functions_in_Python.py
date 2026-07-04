def swap_first_last(lst):
    new_list = lst.copy()
    if len(new_list) >= 2:
        new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list

if __name__ == "__main__":
    original_list = [1, 2, 3, 4]
    swapped_list = swap_first_last(original_list)
    print("Original list:", original_list)  # Output: Original list: [1, 2, 3, 4]
    print("Swapped list:", swapped_list)    # Output: Swapped list: [4, 2, 3, 1]