# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named increment_dict that takes a dictionary and an integer\
# as arguments. It will increment each value by the second argument and return\
# the dictionary.


def increment_dict(my_dict, my_int):
    for my_key in my_dict:
        my_dict[my_key] += my_int
    return my_dict


# print("Except/Results:")
# print("{'Game of Thrones': 11, 'The simpsons': 34, 'Friends': 13, 'X-Files'\
# : # 14}")
# print(increment_dict({'Game of Thrones': 8, 'The simpsons': 31, 'Friends\
# ': 10, 'X-Files': 11}, 3))
# print("Except/Results:")
# print("{'rdm-keyvsvzjdro': -60, 'rdm-keyraxsjxpg': -69, 'rdm-keypknirvul': \
# -92, 'rdm-keyeiqzdbrv': -19, 'rdm-keyjgydfoiz': -100}")
# print(increment_dict({'rdm-keyvsvzjdro': -29, 'rdm-keyraxsjxpg': -38, 'rdm-\
# keypknirvul': -61, 'rdm-keyeiqzdbrv': 12, 'rdm-keyjgydfoiz': -69}, -31))
