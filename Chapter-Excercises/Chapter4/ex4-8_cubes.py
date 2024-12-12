# Make a list of the first 10 cubes and use a 'for loop' to print each value of each cube
cubes = []

for cube in range(1, 11):
    value = cube**3
    cubes.append(value)
print(cubes)

