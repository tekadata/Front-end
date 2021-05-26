#  commun_alphabet

# Write a function named commun_alphabet that takes 2 strings
#  as arguments.

# It will return a list (ordered alphabetically) of the lowercase
#  characters found in both strings.

def commun_alphabet(par_1_string, par_2_string):
    # print(par_1_string)
    # print(par_2_string)
    my_list = []
    lower_char = "azertyuiopqsdfghjklmwxcvbn"
    my_string_1 = sorted(par_1_string)
    my_string_2 = sorted(par_2_string)
    # print(my_string_1)
    # print(my_string_2)
    # print(my_string_2)
    for char in my_string_1:
        # print('char in my_string_1', char)
        if char in my_string_2:
            # print('char in my_string_2', char)
            if char in lower_char:
                # print('char in lower_char', char)
                if char not in my_list:
                    # print('not char in my_list', char)
                    my_list.append(char)
    return my_list


# print(commun_alphabet("bonjour tout le monde", "Hello world"))
# print("['d', 'e', 'l', 'o', 'r']")

# print(commun_alphabet("bonjour tout le monDe!", "HEllo worlD!"))
# print("['l', 'o', 'r']")

# print(commun_alphabet("AZERTHdsdsryZ", "325TYMVHV5MVZY 3.51.dsdsworld"))
# print("['d', 's', 'y']")

# print(commun_alphabet("azertyuiytgfZERT", "AZRETARTEYTRATEnbvcx!"))
# print("[]")
