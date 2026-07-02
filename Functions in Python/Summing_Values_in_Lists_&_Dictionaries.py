def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
    
# Define a function to sum values in a dictionary
def dict_list(d):
    total_dict = 0
    for value in d.values():
        total_dict += value
    return total_dict

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    d = {1: 10, 2: 20, 3: 30}
    
    sum_lst = sum_list(lst)
    dict_list = dict_list(d)

    print("Sum of list:", sum_lst)   # Output: 15
    # Print sum of values in the dictionary
    print("Sum of dictionary:", dict_list) # Output: 60