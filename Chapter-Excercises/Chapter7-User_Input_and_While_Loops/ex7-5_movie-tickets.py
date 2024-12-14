while True:
    prompt = "How old are you?"
    prompt += "\nType 'q' to quit: "
    
    age = input(prompt)
    age = int(age)

    if age == 'q':
        break
    elif age < 3:
        print("Your ticket is free.")
    elif 3 > age < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
    