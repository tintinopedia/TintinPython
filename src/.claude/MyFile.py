cars = {"BMW":"888888","MERCEDES":"10000","Audi":"19999"}
for key in cars:
    print(key)
for value in cars.values():
    print(value)
for key, value in cars.items():
    print(key, ":", value)
key = ["BMW","MERCEDES"]
new_dict = dict.fromkeys(key)
print(new_dict)
cars.popitem()
print(cars)
car = cars.copy()
print(car)
cars.clear()
print(cars)
cars.setdefault("BMW","888888")
print(cars)