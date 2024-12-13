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
        'last_name': 'Cheers',
        'age': 30,
        'city': 'Davie',
    }
]

for x in people:
    for k,v in x.items():
        print(f"{k}:{v}")
    print()