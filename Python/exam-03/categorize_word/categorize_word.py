# categorize_word

# Write a function named categorize_word that takes a string
# as argument. The function will do, in this order:

#     if the string starts with a #,
#      it will print hashtag
#     else if the string starts with a @,
#      it will print login
#     else if the string ends with a .,
#      it will print abbreviation

def categorize_word(par_string):
    # print(par_string)
    if par_string[0] == '#':
        print("hashtag")
    elif par_string[0] == '@':
        print("login")
    elif par_string[-1] == '.':
        print("abbreviation")


# categorize_word("#python")
# print("excpected: hashtag")
# categorize_word("@gvanrossum")
# print("excpected: login")
# categorize_word("Mr.")
# print("excpected: abbreviation")
# categorize_word("#Mr.")
# print("excpected: hashtag")
# categorize_word("something else")
# print()

# categorize_word("#random_string-ehbpacuk")
# print("excpected: hashtag")
# categorize_word("@random_string-ncevfwao")
# print("excpected: login")
# categorize_word("random_string-ptdafzjn.")
# print("excpected: abbreviation")
# categorize_word("#random_string-zqfnvydn.")
# print("excpected: hashtag")
# categorize_word("@random_string-rlrwhfae.")
# print("excpected: login")
# categorize_word("random_string-mdgohcxw")
# print()
