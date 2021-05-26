# concat_small_elements

# Write a function named concat_small_elements that
#  takes a list of strings as argument and returns a string.

# The returned string will be the concatenation of
#  all elements whose length is strictly less than 5.
# The concatenated elements must be in the same order than
#  in the first list.

def concat_small_elements(par_string_list):
    my_string = ''
    max_len = 5
    for item in par_string_list:
        if len(item) < max_len:
            my_string += item
    return my_string


# print(concat_small_elements(["The", "right", "man", "in", "th\
# e", "wrong", "place", "can", "make", "all", "the", "differenc\
# e", "in", "the", "world"]))
# print("Themaninthecanmakealltheinthe")
# print(concat_small_elements(["The", "12345", "man", "in", "th\
# e", "wrong", "place", "can", "make", "all", "the", "differenc\
# e", "in", "", " "]))
# print("Themaninthecanmakeallthein ")
# print(concat_small_elements(["", " "]))
# print(" ")
# print(concat_small_elements([""]))
# print("")
