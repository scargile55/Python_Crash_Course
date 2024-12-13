# Assign three cities in a dictionary as keys to a variable
cities = {
    'Atlanta': {
        'country': 'usa',
        'population': 2_839_848,
        'fact': 'Great places to eat',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 5_345_323,
        'fact': 'Very clean',
    },
    'Brazil': {
        'country': 'South America',
        'population': 1_234_432,
        'fact': 'Most beautiful women',
    }
}

# Print the name of each city and all the info stored about it
for k,v in cities.items():
    print(f"{k}:")
    for info,notes in v.items():
        print(f"{info}: {notes}")
    print()
       