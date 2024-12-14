# Prompt asks user to pick a number
prompt = input("Pick a number to see if it's a multiple of 10: ")
prompt = int(prompt)

# If-statement checks if users number has a remainder
if prompt % 10 == 0:
    print(f"{prompt} is a multiple of 10")
else:
    print(f"{prompt} is not a multiple of 10.")