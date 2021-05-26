# 234567 10 234567 20 234567 30 234567 40 234567 50 234567 60 234567 70 2345679
# Step 1.2
def delete_words(grid_string, word_list):
    pass
    string_end = len(grid_string)
    word_start = string_end - 1
    print("remove_words_in_line:")
    print("len(par_word_list): ", len(word_list))
    # Forward
    for word in word_list:
        word_start = grid_string.find(str(word))

        if word_start > 0 and word_start < string_end:
            print("found word '", word, "'' in '", grid_string,
                  "' at position: ", word_start,
                  " which length: ", len(word))
            word_list.remove(word)
    # g = []
    # for ligne in file:
    #     l = []
    #     for c in str_line:
    #         l.append(c) 
    #     for c2 in l:

    #     g.append(l)  

    grid_list = []
    reversed_grid_string = ''
    for char in grid_string:
        grid_list.append(char)
        print("grid_list: ", grid_list)
    word_start = string_end - 1
    # Backward
    print(grid_string)
    for char in reversed(grid_list):
        reversed_grid_string += char
    print("reversed_grid_string: ", reversed_grid_string)
    # print("len(pcis: ", len(par_character_string))
    # print(par_character_string)
    # print(line_char_list)
    # for i in range (string_length-1):
    #     print("-1-i=",-1-i," i=",i," car: ", par_character_string[i])
    #     reversed_string[-1-i] = par_character_string[i]
    # print (reversed_string)
    for word in word_list:
        word_start = grid_string.find(str(word))
        print("in word '", word, "'' in '", grid_string,
              "' at position: ", word_start,
              " which length: ", len(word))
        if word_start > 0 and word_start < string_end:
            print("found word '", word, "'' in '", grid_string,
                  "' at position: ", word_start,
                  " which length: ", len(word))
            word_list.remove(word)    

    return word_list

# Step 1.1
file = open('./grid', 'r')
file_string = file.read()
file.close()
word_list = []
file = open('./words.dic', 'r')
for file_line in file:
    word_list.append(file_line[:-1])
print("file_string ", file_string)
print("word_list ", word_list)
# Step 1.2
word_list = delete_words(file_string, word_list)
print("returned word_list:\n", word_list)
print("returned word_list number:\n", len(word_list))
