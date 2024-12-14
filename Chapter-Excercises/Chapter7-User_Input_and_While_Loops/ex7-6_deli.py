sandwich_orders = [
    'philly cheese',
    'turkey',
    'ham',
    'jerk chicken',
    'shrimp',
]

finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)

    print(f"I made your {sandwich_order} sandwich.")
print()

print("All the following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich}")