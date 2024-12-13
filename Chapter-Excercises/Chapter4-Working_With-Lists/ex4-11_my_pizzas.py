pizzas = ['sausage', 'cheese', 'vegan']

# Make a copy of original pizza
friends_pizzas = pizzas[:]

# Add new pizzas to each list
pizzas.append('bbq')
friends_pizzas.append('seafood')

# Loop through each list and print names
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print()
print("My friends favorite pizza are:")
for friend_pizza in friends_pizzas:
    print(friend_pizza)