# Create a list and assign it to variable
usernames = ['Major', 'Charlene', 'Steve', 'Admin', 'Erric']

# For-loop checks if the variable is 'admin' which prints a specific response
for user in usernames:
    if user == 'Admin':
        print(f"Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in.")