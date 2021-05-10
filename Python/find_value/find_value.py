# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named find_value that takes a dictionary and a key\
# (as a string) as arguments, and returns the value associated to the key\
# if the key exists; None otherwise.


def find_value(dico, key):
    try:
        # Return key by index from dictionary dico
        return dico[key]
    except KeyError:
        # Catch KeyError exception and return None
        return None


# print(find_value({'Obama': 1961, 'JFK': 1917, 'Trump': 1946, 'Clinton\
# ': 1946, }, 'JFK'))
# print(find_value({'Obama': 1961, 'JFK': 1917, 'Trump': 1946, 'Clinton\
# ': 1946, }, 'Nixon'))
