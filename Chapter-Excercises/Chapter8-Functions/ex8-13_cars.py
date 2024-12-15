def make_car(manufacturer, model, **random):
    random['manufacturer'] = manufacturer
    random['model'] = model
    return random

car = make_car('Ford', 'Mustang', color='black', tow_package=True)
print(car)

