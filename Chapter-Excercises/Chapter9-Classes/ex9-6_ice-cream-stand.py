class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} sells the best {self.cuisine_type} food.")
        print(f"{self.restaurant_name.title()} served {self.number_served} people today.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is finally open!")
    
    def set_number_served(self, amount):
        self.number_served = amount
    
    def increment_number_served(self):
        self.number_served += 100

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, 'desserts')
        self.flavors = [
            'chocolate',
            'strawberry',
            'vanilla',
            'lemon',
        ]
    
    def display_flavors(self):
        print(f"{self.restaurant_name} best ice cream flavors are: ")

        for x in self.flavors:
            print(f"{x}")

rest_icecream = IceCreamStand('Rosy', 'desserts')

rest_icecream.display_flavors()