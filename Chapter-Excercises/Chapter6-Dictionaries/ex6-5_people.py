# Nest three dictionaries into a list
people = [
    {
        'first_name': 'Major',
        'last_name': 'Jones',
        'age': 32,
        'city': 'Albany'
    },
    {
        'first_name': 'Brandon',
        'last_name': "Davidson",
        'age': 31,
        'city': 'Patterson',
    },
    {
        'first_name': 'Micah',
        'last_name': 'Cheerss',
        'age': 30,
        'city': 'Davie',
    }
]

# Loop through list to print everything about that person
for x in people:
    for k,v in x.items():
        print(f"{k}:{v}")
    print()