# Assign dictionary to variable
rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'amazon': 'south america'
}

# Print each piece of information
for k,v in rivers.items():
    print(f"The {k.title()} river runs through {v.title()}")