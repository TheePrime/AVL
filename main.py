from Cart import Cart

#initialize the cart
cart = Cart()
# Add item to cart
cart.add_item('apple', 1.5)

print(cart.total_items())
print(cart.total_price())
print(cart.search_item('apple'))
