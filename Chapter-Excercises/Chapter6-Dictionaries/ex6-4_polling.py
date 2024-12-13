# Assign dictionary to variable
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Assign dictionary to variable
names = [
    'major',
    'brandon',
    'edward',
    'steve',
    'jen',
]

# Loop through list to validate who has taken the poll already
for name in names:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for already taking this poll.")
    else:
        print(f"Please take our poll {name.title()}.")