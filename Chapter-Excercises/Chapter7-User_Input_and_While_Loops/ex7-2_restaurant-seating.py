# Ask user a specefic question
prompt = input("How many people are in your dinner group? ")

# Converts prompt to an integer
prompt = int(prompt)

# If-statement confirms if group is larger than eight
if prompt > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")