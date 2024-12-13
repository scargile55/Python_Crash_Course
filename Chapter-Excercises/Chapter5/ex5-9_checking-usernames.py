# Create a list and assign it to variable
current_users = ['Erric', 'Chris', 'John', 'Steve', 'Darius']
new_users = ['Major', 'John', 'Brandon', 'Chris', 'Ashton']

# For-loop checks if any new users are in current users and prints specific response
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is already in our system, please choose a unique username.")
    else:
        print(f"{new_user} is available to use.")