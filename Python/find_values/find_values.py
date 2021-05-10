# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named find_values that takes a dictionary and \
# a list of keys (as a list of strings) as arguments, and returns \
# the list of values associated to the keys
# In the returned list, you will put the value if the key exists; \
# None otherwise
# The returned values must be in the same order as the list of keys


def find_values(my_dict, my_lokeys):
    my_lovalues = []
    for my_key in my_lokeys:
        if my_dict.get(my_key) is not None:
            my_lovalues.append(my_dict.get(my_key))
        else:
            my_lovalues.append(None)
    return my_lovalues


# print("Excpected: [1917, None, 1961] = ", find_values({'Obama': 1961, 'JFK\
# ': 1917, 'Trump': 1946, 'Clinton': 1946, }, ['JFK', 'Nixon', 'Obama']))
