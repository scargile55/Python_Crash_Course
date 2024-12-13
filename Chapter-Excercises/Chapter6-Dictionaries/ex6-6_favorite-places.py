# Assign dictionary containing a list to a variable
favorite_places = {
    'Charlene': ['Africa', 'California', 'New York'],
    'Robert': ['New Zealand'],
    'John': ['India'],
}

# Loop through dictionary to print each person's favorite place
for k,v in favorite_places.items():
    print(f"{k}'s favorite places are:")
    for place in v:
        print(f"{place}")
    print()