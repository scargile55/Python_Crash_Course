class Users:
    def __init__(self, first_name, last_name, middle_name, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.occupation = occupation
    
    def describe_user(self):
        full_name = f"{self.first_name} {self.middle_name} {self.last_name}"
    
        print(f"{full_name} is our new {self.occupation} ")
        return full_name
        
    def greet_user(self):
        print(f"Hello {self.first_name.title()}, welcome to the team!")

user1 = Users('Simeon', 'Cargile', 'Cameron', 'cloud engineer')
user2 = Users('Major', 'Jones', 'Jamar', 'teacher')

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
