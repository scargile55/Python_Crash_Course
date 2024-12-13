favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

names = [
    'major',
    'brandon',
    'edward',
    'steve',
    'jen',
]

for name in names:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for already taking this poll.")
    else:
        print(f"Please take our poll {name.title()}.")