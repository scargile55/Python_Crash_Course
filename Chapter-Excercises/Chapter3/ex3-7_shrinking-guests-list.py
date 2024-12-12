# Extend code from excercise 3-6
guest_list = ['playboi carti', 'kanye', 'kendrick lamar']

print(f"{guest_list[0].title()} is invited to my dinner.")
print(f"{guest_list[1].title()} is invited to my dinner.")
print(f"{guest_list[2].title()} is invited to my dinner.")
print()
print("Kanye said he will be too busy to attend")
print()

guest_list[1] = "ken carson"

print(f"{guest_list[0].title()} is invited to my dinner.")
print(f"{guest_list[1].title()} is invited to my dinner.")
print(f"{guest_list[2].title()} is invited to my dinner.")
print()
print("Great news, I have a bigger table!!")
print()

# Use insert and append to add names to list
guest_list.insert(0, 'drake')
guest_list.insert(3, 'pharrell')
guest_list.append('lil uzi')

# Use 'for loop' to print each new invite in guest list 
for x in guest_list:
    print(f"{x.title()} is invited to my dinner.")
print()

# Shrink guest list using 'pop' and print a message each time.
print("I can only two people now.")
names = guest_list.pop()
print()
print(f"Sorry {names.title()}, I have to uninvite you.")
names = guest_list.pop()
print(f"Sorry {names.title()}, I have to uninvite you.")
names = guest_list.pop()
print(f"Sorry {names.title()}, I have to uninvite you.")
names = guest_list.pop()
print(f"Sorry {names.title()}, I have to uninvite you.")
print()

# Print the list of the remaining guests
print(f"{guest_list[0].title()} is still invited to my dinner.")
print(f"{guest_list[1].title()} is still invited to my dinner.")

# Delete the remaining guests of the list
del(guest_list[1])
del(guest_list[0])
print()
print(guest_list)


