# State which guest who can't make it and replace them
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