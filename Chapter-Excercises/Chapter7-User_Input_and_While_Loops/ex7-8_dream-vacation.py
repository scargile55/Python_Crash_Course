# Empty dictionary
responses = {}

# Assign variable to True
polling_active = True

# While variable is set to true, the loop will continue
while polling_active:
    name = input("What's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    
    # Add key-value to dictionary
    responses[name] = response

    repeat = input("Does anyone else want to take our poll? (yes/no)")
    if repeat == 'no':
        polling_active = False

# Loops through and prints key-value from dictionary
for k, v in responses.items():
    print(f"{k} wants to visit {v}")