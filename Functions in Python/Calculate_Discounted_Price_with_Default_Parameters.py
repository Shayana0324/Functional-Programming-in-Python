# define the calculate_discount function with parameters price, discount (default 10) and tax (default 5)

def calculate_discount(price, discount=10, tax=5):
    
    discount_amount = price * (discount / 100)
    price_after_discount = price - discount_amount
    tax_amount = price_after_discount * (tax / 100)
    final_price = price_after_discount + tax_amount
    return final_price

    
if __name__ == "__main__":
    price = 100
    discount, tax = 10, 5
    final_price = calculate_discount(price)
    print("Final price:", final_price) # Final price: 94.5
    
    final_price = calculate_discount(60)
    print("Final price:", final_price) 
    
    final_price = calculate_discount(price, 20, tax)
    print("Final price:", final_price)
    
    final_price = calculate_discount(price, discount, 6)
    print("Final price:", final_price)
    
    final_price = calculate_discount(100, discount=15, tax=10)
    print("Final price:", final_price)
