usernames = ['Major', 'Charlene', 'Steve', 'Admin', 'Erric']

if not usernames:
    print("We need to find some users!")
for user in usernames:
    if user == 'Admin':
        print(f"Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in.")