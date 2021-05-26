# 234567 10 234567 20 234567 30 234567 40 234567 50 234567 60 234567 70 2345679
# Step 1.1 first: get game data. 
# Step 1.1.1 Open 'words.dic' file and set words into a list - par_hidden_words
# Step 1.1.2 Open 'grid' file and set content line by line into a list of lists
# Step 1.2 Next: write function check_line
# Step 1.2.1 check if a given line of letters contains any of the hidden words.
# /!\ Word can be read/found in both directions of the line of letters.
# Step 1.2.2 you need to check a line in both directions.
# Step 1.2.3 found hidden word must be removed from par_hidden_words
# Step 1.3 Once: write function check_grid
# Step 1.3.1 iterate over all the lines (horizontal and vertical) 
# Step 1.3.2 and check them one by one with the check_line function
# Step 1.4 When you have finish your iterations over the whole grid, 
# whatever words remain in the par_hidden_words list have not been found. 
# You should print those words (in the initial order of the file) and 
# you are done for step 1!  


# Step 1.1 open_file function, parameters: file name, access rights, read method
def open_file(par_file_name='./words.dic',
              par_access_rights='r',
              par_read_method=2):
    try:
        # all_lines_list: list returned by the function 
        all_lines_list = []
        if par_read_method == 1:
            # print("read method #1: line by line")
            file = open(par_file_name, 'r')
            # print("open the file: ", par_file_name)
            # print("for line in file:")
            for line in file:
                # print("append line: ", line[:-1])
                all_lines_list.append(line[:-1])
            # print("close the file: ", par_file_name)
            file.close()

        elif par_read_method == 2:
            # print("read method #2: list out of the lines")
            file = open(par_file_name, 'r')
            # print("open the file: ", par_file_name)            
            # print("read file and list out of the lines with .readlines()")
            all_lines_list = file.readlines()
            # print("all_lines_list: ", all_lines_list)
            # print("close the file: ", par_file_name)
            file.close()

        elif par_read_method == 3:
            # print("read method #3: all the content at once")
            file = open(par_file_name, 'r')
            # print("read all the content at once")
            string_content = file.read()
            all_lines_list.append(string_content)
            # print("string_content: ", string_content)
            # print("close the file: ", par_file_name)
            file.close()

        # print("list_all_lines: ", all_lines_list)
        return all_lines_list

    except (FileNotFoundError, IOError):
        print("except: (FileNotFoundError, IOError)")

    # finally:
        # print("finally: ")


# 234567 10 234567 20 234567 30 234567 40 234567 50 234567 60 234567 70 2345679
# Step 1.2 Next: write function check_line
def check_line(par_grid_line, par_hidden_words):
    # print("check_line(par_grid_line", par_grid_line)
    # print(" , par_hidden_words):", par_hidden_words)
    # for character in par_grid_line:
    # print("for character in par_grid_line:", character)
    length = len(par_grid_line)
    position = length - 1
    # print("check_line:")
    # print("len(par_hidden_words): ", len(par_hidden_words))

# Step 1.2.1 check if a given line of letters contains any of the hidden words.  
    # Forward
    found_words = []
    for word in par_hidden_words:
        position = par_grid_line.find(str(word))

        if position > 0 and position < length:
            print(word)
            # print("found word '", word,
            #       "' at position: ", position,
            #       " which length: ", len(word))
            i = 0
            for char in word:
                # print("char position in found_words ", position + i)
                # if not found_words.get(position + i):
                found_words.append(position + i)
                i += 1
            # Step 1.2.3 found hidden word must be removed from par_hidden_words    
            par_hidden_words.remove(word)

    # /!\ Word can be read/found in both directions of the line of letters.
    # Step 1.2.2 you need to check a line in both directions.
    # Backward
    line_char_list = []
    line_char_string = ''
    for character_in_list in par_grid_line:
        line_char_list.append(character_in_list)
        # print("line_char_list: ", line_char_list)
    position = length - 1
    # print(par_grid_line)
    for character_in_list in reversed(line_char_list):
        line_char_string += character_in_list
        # print("line_char_string: ", line_char_string)
    for word in par_hidden_words:
        # print("word: ", word)
        position = line_char_string.find(str(word))
        # print("position: ", position)
        if position > 0 and position < length:
            print(word)
            print("found word '", word,
                  " at position: ", position,
                  " which length: ", len(word))
            i = 0
            for char in word:
                # print("char position in found_words ", position + i)
                # if not found_words.get(position + i):
                found_words.append(position + i)
                i += 1
    # Step 1.2.3 found hidden word must be removed from par_hidden_words        
            par_hidden_words.remove(word)          
    return par_hidden_words

# Step 1.3 Once: write function check_grid
# Step 1.3.1 iterate over all the lines (horizontal and vertical) 
# Step 1.3.2 and check them one by one with the check_line function
def check_grid(par_grid, par_grid_list, par_hidden_words):
    grid_lol=[]
    for list in par_grid_list:
        for char in list:
            grid_lol.append(char)
    # print("grid list of lists ", grid_lol)
    for row in grid:
        # print("word in grid: ", line)
        # print("par_hidden_words: ", par_hidden_words)
        # print("par_hidden_words number:\n", len(par_hidden_words))
        print()
        print("hidden words in grid:")
        print()
        # Step 1.2 Next: write function check_line
        par_hidden_words = check_line(row, par_hidden_words)
    # print("returned par_hidden_words:\n", par_hidden_words)
    # print("returned par_hidden_words number:\n", len(par_hidden_words))
    # print("found hidden words characters to high-light ", sorted(found_words))
    print()
    print(len(par_hidden_words), " not found par_hidden_words:\n\n", \
          par_hidden_words)
    print()

    # Step 3 - Advanced

    # For this final step, you will print back the grid after having replaced all \
    # the hidden words by their uppercase version. Only letters that are not part \
    # of any words should remain in lowercase.
    found_grid_lol =[]
    for posi, char in enumerate(grid_lol):
        # print("char ", char, "posi ", posi)
        if posi in found_words:
            found_grid_lol.append(char.upper())  
        else:
            found_grid_lol.append(char)
    result_grid_lol = []
    line = ''
    i = 0
    while i < posi:
        for char in found_grid_lol[i]:
            if char != '\n':
                line += char
            else:
                line += char
                # print('line', line)
                result_grid_lol.append(line)
                line=''
            i += 1
    print()
    print("grid")
    print()
    for line in grid_list:
        print(line, end='')
    print('\n')
    print("Found Words in Uppercase in grid ")
    print()
    for line in result_grid_lol:
        print(line, end='')
    print()  
    return par_hidden_words

# 234567 10 234567 20 234567 30 234567 40 234567 50 234567 60 234567 70 2345679
# Test of open_file function for the 3 read methods:
# list = open_file(par_read_method=1)
# print(list)
# list = open_file(par_read_method=2)
# print(list)
# list = open_file(par_read_method=3)
# print(list)

# Step 1.1 first: get the game data. 
# Step 1.1.1 Open the 'words.dic' file and set words into a list - hidden_words
hidden_words = open_file(par_file_name="./words.dic",
                             par_read_method=1)
print()
print(len(hidden_words), " par_hidden_words to find:\n\n", hidden_words)
print()
# for word in hidden_words:
# print("word in hidden_words: ", word)
# print("character in hidden_words: ", character)
# print()

# Step 1.1.2 Open the 'grid' file and set all the content at once
grid = open_file(par_file_name="./grid",
                 par_read_method=3)
# print("grid:\n", grid)

# Step 1.1.2 Open the 'grid' file and set content line by line
grid_list = open_file(par_file_name="./grid",
                      par_read_method=2)
# print("grid_list:\n", grid_list)

# Step 1.3 Once: write function check_grid
hidden_words = check_grid(par_grid=grid,
                          par_grid_list=grid_list, 
                          par_hidden_words=hidden_words)



