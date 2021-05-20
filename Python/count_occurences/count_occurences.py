# Write a function named count_occurrences that takes a string
# as argument and returns a list with the number of occurrences
# for each word in the string.
# The list will have a tuple (occurrences, word) for each word.
# A word will be defined as a sequence of alphabet characters
# separated by a space () or a comma (,).
# The strings sent to the function will only contain words,
# spaces and commas.

def count_occurrences(par_string):
    # init result list as empty
    result = []
    # replace all comas of par_string into my string
    my_string = par_string.replace(' ', ',')
    print(my_string)
    # split all words of my_string into a list of string
    my_string = my_string.split(',')
    print(my_string)
    # for each word in my_string set as item
    for item in my_string:
        print(item, len(item))
        if len(item) > 0:
            # coutn each occurence(s) of item word in my string
            number = my_string.count(item)
            print(number)
            # create a tuple immutable of (occurences, item)
            my_tuple = (number, item)
            # add into my resul list the tuple
            result.append(my_tuple)
            print(my_tuple)
            # if number of occurences of item in my string is > 1
            # while multiple occurences of an item in my string exist
            print("nb occu to del a", number)
            # while number > 0:
            #     # remove the other occurences of my string
            #     my_string.remove(item)
            #     print("remove", item)
            #     print("nb occu to del b", number)
            #     number -= 1
            #     print("nb occu to del c", number)
            #     print(my_string)
        else:
            print("else", item)
    print("result a", result)

    number = len(result) - 1
    print("result, len(result)", result, len(result))
    my_list = []

    while number >= 0:
        my_list.append(result[number])
        number -= 1
    print("my_list", my_list)

    # for each word in my_string set as item
    for item in my_string:
        print(item, len(item))

        # coutn each occurence(s) of item word in my string
        number = my_string.count(item)
        print(number)
        # create a tuple immutable of (occurences, item)
        my_tuple = (number, item)
        # add into my resul list the tuple
        result.append(my_tuple)
        print(my_tuple)
        # if number of occurences of item in my string is > 1
        # while multiple occurences of an item in my string exist
        print("nb occu to del a", number)
        while number > 0:
            # remove the other occurences of my string
            my_string.remove(item)
            print("remove", item)
            print("nb occu to del b", number)
            number -= 1
            print("nb occu to del c", number)
            print(my_string)

    print("my_list.sort():", my_list)
    for item in result:
        number = result.count(item)
        if number > 1:
            result.remove(item)
    print("result b", result)
    return result


print(count_occurrences("hey, hey, hey"))
print("[(3, 'hey')]")

print(count_occurrences("it was a beautiful day, not too hot, not too cold"))
print("[(1, 'it'), (1, 'was'), (1, 'a'), (1, 'beautiful'), (1, 'day\
    '), (2, 'not'), (2, 'too'), (1, 'hot'), (1, 'cold')]")

print(count_occurrences(" "))
print("[]")
