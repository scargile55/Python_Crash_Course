# Extend code from excercise 3-5
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