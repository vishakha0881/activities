'''Problem 1:

Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.
'''
def calculate_discounted_price(amount, is_prime_member):
    discount = 0.0
    if is_prime_member:
        discount += 0.15
    discount += 0.08
    discounted_amount = amount * (1 - discount)
    return discounted_amount
print(calculate_discounted_price(100, True))