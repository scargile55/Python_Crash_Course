def sandwiches(*toppings):
    for x in toppings:
        print(f"Your sandwich contains {x}.")

sandwiches('tuna', 'beef', 'ham', 'cheese', 'turkey')
print()
sandwiches('banana peppers', 'olives')