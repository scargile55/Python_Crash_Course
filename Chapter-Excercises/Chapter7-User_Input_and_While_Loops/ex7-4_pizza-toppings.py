# While-loop asks user to provide input
while True:
    prompt = "Tell me what kind of toppings you want on your pizza."
    prompt += "\nEnter 'q' to quit: "

    topping = input(prompt)

    if topping == 'q':
        break
    else:
        print(f"I will add {topping} to your pizza.")

