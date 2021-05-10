# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named create_week_dict that takes no arguments, and returns\
# a dictionary. The dictionary will have all days of the week as keys, and 0 \
# as value for each key.
# The day of the week will be written monday, tuesday, wednesday, thursday, \
# friday, saturday and sunday.


def create_week_dict():
    week_dict = {'monday': 0, 'tuesday': 0, 'wednesday': 0}
    # update() method: add all elements of a dictionary to another dictionary
    week_dict.update({'thursday': 0, 'friday': 0})
    week_dict.update({'saturday': 0, 'sunday': 0})
    return week_dict


# Test create_week_dict()
# print("Test create_week_dict()\n", create_week_dict())
