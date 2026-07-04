# Modifying the append_zero Function to Return a New List
def append_zero(lst):
    new_list = lst.copy()   # Create a copy of the original list
    new_list.append(0)      # Append 0 to the copy
    return new_list

if __name__ == "__main__":
    # modify the function call and print both original and updated lists
    original_list = [1, 2, 3]
    new_list = append_zero(original_list)

    print("Original list:", original_list)  # [1, 2, 3]
    print("New list:", new_list)            # [1, 2, 3, 0]