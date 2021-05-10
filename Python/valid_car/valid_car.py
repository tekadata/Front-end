# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named valid_car that takes a dict representing a car \
# as argument, and throws the following exceptions:
#    if the car is not a dict, it will throw a TypeError with the message\
# "This variable isn't representing a car..."
#    if the car has no key name or if the key name has a blank value, \
# it will throw a ValueError with the message "This car has no name"
#    if the car has a distance larger than 500 thousands, it will throw \
# a ValueError with the message "This car is too old!!!"


def valid_car(my_dict):
    try:
        return my_dict
    except TypeError:
        print("This variable isn't representing a car..")
    except ValueError:
        print("This car has no name")
    except ValueError:
        print("This car is too old!!!")


# print(valid_car({"name": "DeLorean", "distance": 12345}))
