class Restauraunt:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} sells the best {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is finally open!")

new_restaraunt = Restauraunt('Roscoes', 'soul')

new_restaraunt.describe_restaurant()
new_restaraunt.open_restaurant()