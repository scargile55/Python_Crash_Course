class Restauraunt:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} sells the best {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is finally open!")

seafood_restaurant = Restauraunt('gumby', 'seafood')
steak_restaurant = Restauraunt('sals', 'country')
chinese_restaurant = Restauraunt('long hei', 'chinese')

seafood_restaurant.describe_restaurant()
steak_restaurant.describe_restaurant()
chinese_restaurant.describe_restaurant()