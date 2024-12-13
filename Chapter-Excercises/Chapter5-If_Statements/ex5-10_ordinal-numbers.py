# Assign numbers 1-9 to a variable
numbers = list(range(1, 10))

# For-loop prints the proper oridanl ending for each number
for x in numbers:
    if x == 1:
        print(f"{x}st")
    elif x == 2:
        print(f"{x}nd")
    elif x == 3:
        print(f"{x}rd")
    else:
        print(f"{x}th")