# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named update_value that takes a dictionary, a key and \
# a value as arguments.
# It will update the value at the given key, with the value provided \
# as argument. If the key doesn't exist, it will create it.
# The function returns the updated dictionary.


def update_value(dico, key, val):
    try:
        # Upsdate the dictionary the associated value of the given key
        # with the given value
        dico[key] = val
        # return the updated dictionary
        return dico
    except KeyError:
        # If the key doesn't exist, create it
        dico.update({key, val})
        # return the updated dictionary
        return dico


# Test update_value()
print(update_value({'Bread': 1, 'Salad': 1, 'Tomato': 2, 'Onion': 0}, '\
Onion', 3))
print(update_value({'Bread': 1, 'Salad': 1, 'Tomato': 2}, 'Mayonnaise\
', 1))
