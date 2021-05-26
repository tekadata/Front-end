#  only_digits

# Write a function named only_digits that takes a string
# as argument and returns True if the string is only
# made of digits and spaces; False otherwise.

def only_digits(par_string):
    is_true = True
    # print("string to check:",par_string)
    for char in par_string:
        if not(char.isdigit() is True or char == ' '):
            # print("char is digit ?", char, False)
            is_true = False
        # else:
        #     print("char is digit ?", char, True)
    if len(par_string) == 0:
        is_true = False
        # print("string empty!", len(par_string))
    return is_true


# print(only_digits("100 299 009"))
# print("return:", True)

# print(only_digits("666"))
# print("return:", True)

# print(only_digits("Number: 0900 099 898"))
# print("return:", False)

# print(only_digits(""))
# print("return:", False)

# print(only_digits(" @0"))
# print("return:", False)

# print(only_digits(":=.+/Ûåå"))
# print("return:", False)

# print(only_digits("            "))
# print("return:", True)
