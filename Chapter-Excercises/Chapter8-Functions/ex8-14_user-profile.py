def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Simeon', 'Cargile', city='Atlanta', color='black', occupation='Cloud Engineer')
print(user_profile)