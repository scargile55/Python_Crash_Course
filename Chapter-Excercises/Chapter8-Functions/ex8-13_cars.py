def make_car(manufacturer, model, **random):
    """Creates a dictionary with any arbituary arguments the user creates"""
    random['manufacturer'] = manufacturer
    random['model'] = model
    return random

car = make_car('Ford', 'Mustang', color='black', tow_package=True)
print(car)

