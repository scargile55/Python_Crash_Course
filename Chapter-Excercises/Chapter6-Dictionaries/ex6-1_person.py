# Assign dictionary to variable
person = {
    'first_name': 'Major',
    'last_name': 'Jones',
    'age': 32,
    'city': 'Albany'
}

# Print each piece of information
for k,v in person.items():
    print(f"{k}:{v}")