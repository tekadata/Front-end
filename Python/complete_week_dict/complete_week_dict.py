# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named complete_week_dict that takes a dictionary \
# (with the seven days of the week as keys) as argument, \
# and returns a dictionary.
# If a day of the week (monday, tuesday, wednesday, thursday, \
# friday, saturday and sunday) is absent in the dictionary's keys, \
# you will add it with the value 0.


def complete_week_dict(my_dict):
    week_dict = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    week_dict.append('saturday')
    week_dict.append('sunday')
    # print(week_dict)
    for my_key in week_dict:
        if my_key in my_dict:
            pass
        else:
            my_dict[my_key] = 0

    return my_dict


# print("{'monday': 1, 'tuesday': 7, 'saturday': 8, 'sunday\
# ': -7, 'wednesday': 0, 'friday': 0, 'thursday': 0}")
# print(complete_week_dict({'monday': 1, 'tuesday': 7, 'satur\
# day': 8, 'sunday': -7, }))
# print("Except/Result:")
# print("{'monday': 83, 'tuesday': -24, 'wednesday': 10, 'thurs\
# day': -39, 'friday': -2, 'saturday': -97, 'sunday': -21}")
# print(complete_week_dict({'monday': 83, 'tuesday': -24, 'wednes\
# day': 10, 'thursday': -39, 'friday': -2, 'saturday': -97, 'sunday': -21}))
