def add(a, b):
    return a + b

def add_three(x, y, z):
    return x + y + z

if __name__ == "__main__":
    sum_ints = add(2, 3)
    sum_doubles = add(2.5, 3.5)
    
    sum_int_three = add_three(1, 2, 3)
    sum_doubles_three = add_three(3.6, 4.3, 2.5)
    
    # TODO: Define the new function for three integers and call it here to find a sum of 1, 2 and 3

    print("Sum of ints:", sum_ints)       # Sum of ints: 5
    print("Sum of doubles:", sum_doubles) # Sum of doubles: 6.0
    
    # TODO: print the calculated sum of 1, 2 and 3
    print("Sum of three ints:", sum_int_three)
    print("Sum of doubles(three int):", sum_doubles_three)