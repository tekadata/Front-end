# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named print_filter that takes a list and prints all its \
# elements one by one. It also takes a second, optional argument: a list of \
# banned words that should never be printed


def print_filter(my_lov, my_lov_ban=[]):
    for my_item in my_lov:
        if my_item not in my_lov_ban:
            print(my_item)


# ma_liste = [1, '2', 3, ]
# ma_liste_optionnelle = [3]
# print("Except/Result:")
# print(1)
# print('2')
# print(3)
# print_filter(ma_liste)
# print("Except/Result:")
# print(1)
# print('2')
# print_filter(ma_liste,ma_liste_optionnelle)
