sandwich_orders = [
    'philly cheese',
    'pastrami',
    'turkey',
    'pastrami',
    'ham',
    'jerk chicken',
    'pastrami',
    'shrimp',
]

finished_sandwiches = []

print("The Deli has ran out of pastrami.")
print()
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)

    print(f"I made your {sandwich_order} sandwich.")
print()

print("All the following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich}")