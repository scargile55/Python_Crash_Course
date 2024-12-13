# Create a list and assign it to variable
usernames = ['Major', 'Charlene', 'Steve', 'Admin', 'Erric']

# If-statement checks if variable is true or false
if not usernames:
    print("We need to find some users!")

# For-loop checks if the variable is 'admin' which prints a specific response
for user in usernames:
    if user == 'Admin':
        print(f"Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in.")