# This is an example Python file

def get_discounted_price(price, discount):
    """Apply discount and return the final price."""
    final_price = price * (1 - discount)
    return final_price

# Important business logic code starts here
def main():
    original_price = 100
    discount_rate = 0.2
    discounted_price = get_discounted_price(original_price, discount_rate)
    print(f"The discounted price is: ${discounted_price}")

# End of example code
