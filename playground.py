# Unlimited positional arguments
def add(*args):
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum


# print(add(7, 6, 2, 3, 4, 5))

# Unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car()
print(my_car.model)

# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
#
# my_car = Car(model="GTR", make="Nissan")
# print(my_car.model)

