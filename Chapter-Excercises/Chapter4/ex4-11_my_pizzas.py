pizzas = ['sausage', 'cheese', 'vegan']
friends_pizzas = pizzas[:]

pizzas.append('bbq')
friends_pizzas.append('seafood')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print()
print("My friends favorite pizza are:")
for friend_pizza in friends_pizzas:
    print(friend_pizza)