responses = {}

polling_active = True

while polling_active:
    name = input("What's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
  
    responses[name] = response

    repeat = input("Does anyone else want to take our poll? (yes/no)")
    if repeat == 'no':
        polling_active = False

for k, v in responses.items():
    print(f"{k} wants to visit {v}")