class Users:
    def __init__(self, first_name, last_name, middle_name, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.occupation = occupation
        self.login_attempts = 0
    
    def describe_user(self):
        full_name = f"{self.first_name} {self.middle_name} {self.last_name}"
    
        print(f"{full_name} is our new {self.occupation} ")
        return full_name
        
    def greet_user(self):
        print(f"Hello {self.first_name.title()}, welcome to the team!")
    
    def increment_login(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = Users('Simeon', 'Cargile', 'Cameron', 'cloud engineer')

user1.increment_login()
user1.increment_login()
user1.increment_login()
user1.reset_login_attempts()

user1.describe_user()
print(user1.login_attempts)
