# Write a function named encode_str that takes a string as argument
# and encodes it.

# Each series of repeated characters will be replaced by the number
# of occurrences
# followed by the repeated character.
# For example, the sequence aaaa in the original string will be replaced
# by 4a
# in the encoded string.

# The function will return the encoded string.


def encode_str(par_string):
    result = ''
    char_list = []
    print(par_string)
    for char in par_string:
        number = par_string.count(char)
        print("char * number", char, number)
        char_list.append(char)
        if number > 1:
            char_list.append(number)
            # par_string.remove(char)
    print(char_list)
    # while 
    return result


print(encode_str("HELLO!"))
print("'HE2LO!'")

print(encode_str("AAAAAH YYYYMMDD!!!"))
print("'5AH 4Y2M2D3!'")
