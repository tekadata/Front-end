import random
import sys

min_size = 2
hidden_cell = "hidden"
visible_cell = "visible"
hidden_value = '◻️'
bomb_value = '*'
flag_value = 'x'
space = 30
len_hidden = int(len(hidden_value))

def check_argument():
    size = None
    return size

def screen_size(size):
    m_size = grid_size(size)
    if(m_size is None):
        raise ValueError("ValueError : Size must be an integer")
    else:
        width_height = (m_size * len_hidden) + (m_size * space)
    return width_height


def grid_size(size):
    if(size < min_size):
        size = 2
        raise ValueError("ValueError : Size must be strictly superior to 1")
    elif(type(size) is str):
        raise ValueError("ValueError : Size must be a integer")
    else:
        result = size
    return result


def cell_content(content, state):
    cell = " "
    if(content is None and state == hidden_cell):
        cell = empty_value
    elif(content == bomb_value and state == hidden_cell):
        cell = empty_value
    elif(content == bomb_value and state == visible_cell):
        cell = bomb_value
    else:
        cell = content
    return cell


def make_empty_ms_grid(int_size):
    cell_satus = {'content': None, 'state': 'hidden'}
    grid = []
    size = int(int_size)
    # print("size:", size)
    for _ in range(size):
        cells = []
        for _ in range(size):
            cells.append(cell_satus)
        grid.append(cells)    
    return grid


# # Todo: Ajouter des bombes dans la grille vide
# def place_bombs(grid):
#     grid = []
#     return grid
# Todo: Step 3 - Ajouter des bombes dans la grille vide
def place_bombs(grid):
    nb_bomb_max = randomiAze(len(grid))
    stop = 0
    while stop <= nb_bomb_max:
        x = random.randint(0, len(grid)-1)
        y = random.randint(0, len(grid)-1)
        x = int(x)
        y = int(y)
        grid[y].pop(x)
        grid[y].insert(x, {'content': bomb_value, 'state': hidden_cell})
        stop += 1 
    return grid

# Todo: Step 3 - fonction I.A. #2Ouf qui optimise le place-bombs()
def randomiAze(int_size=2, int_difficulty=1):
    try:
        # init du dénominateur + coefficient / facile + bomb = 3
        coef = 9 / 10
        nb_bomb = 3
        # print("int_size", int_size)
        # print("int_difficulty", int_difficulty)
        int_size = int(int_size)
        int_difficulty = int(int_difficulty)
        # print("diff", int_difficulty)
        if int_difficulty == 1:
            # print("diff", int_difficulty)
            if  int_size < 2:
                # print("size<2", int_difficulty) 
                nb_bomb = 1
            if int_size > 10:
                nb_bomb = coef *(int(int_size) + int(int_difficulty))
            else:
                nb_bomb = coef *(int(int_size))
            
        # print("nb_bomb", nb_bomb)

        if nb_bomb > size*2-1:
            nb_bomb = size*2-1

    except Exception:
        pass
    finally:
        return nb_bomb

# Vérifier que la size est > 1, sinon, forcer à 2
def force_min_size(size=2):
    print("size", size)
    if  size < 2:
        # print("size<2", size) 
        size = 2
        # print("size", size)
        return size


def count_bomb_around (grid, x, y):
    cpt = 0
    i_max = len(grid)-1
    # check L cell
    if y >= 0 and y <= i_max and x-1 >= 0 and x-1 <= i_max:
        if check_bomb(grid[y][x-1]):
            cpt +=1
            # print("L Bomb!\nx:",x," y:",y)
    # check LU cell
    if y-1 >= 0 and y-1 <= i_max and x-1 >= 0 and x-1 <= i_max:    
        if check_bomb(grid[y-1][x-1]):
            cpt +=1
            # print("LU Bomb!\nx:",x," y:",y)
    # check U cell
    if y-1 >= 0 and y-1 <= i_max and x >= 0 and x <= i_max:    
        if check_bomb(grid[y-1][x]):
            cpt +=1
            # print("U Bomb!\nx:",x," y:",y)
    # check UR cell
    if y-1 >= 0 and y-1 <= i_max and x+1 >= 0 and x+1 <= i_max:       
        if check_bomb(grid[y-1][x+1]):    
            cpt +=1
            # print("UR Bomb!\nx:",x," y:",y)
    # check R cell
    if y >= 0 and y <= i_max and x+1 >= 0 and x+1 <= i_max:    
        if check_bomb(grid[y][x+1]):    
            cpt +=1
            # print("R Bomb!\nx:",x," y:",y)
    # check RD cell
    if y+1 >= 0 and y+1 <= i_max and x+1 >= 0 and x+1 <= i_max:    
        if check_bomb(grid[y+1][x+1]):
            cpt +=1
            # print("RD Bomb!\nx:",x," y:",y)
    # check D cell
    if y+1 >= 0 and y+1 <= i_max and x >= 0 and x <= i_max:    
        if check_bomb(grid[y+1][x]):
            cpt +=1
            # print("D Bomb!\nx:",x," y:",y)
    # check LD cell
    if y+1 >= 0 and y+1 <= i_max and x-1 >= 0 and x-1 <= i_max: 
        if check_bomb(grid[y+1][x-1]):
            cpt +=1
            # print("LD Bomb!\nx:",x," y:",y)
    return cpt

# Todo: Placer les nombres autours des bombes
def place_numbers(grid):
    # print("place_numbers")
    # parcours de la première ligne de la grille
    y = 0
    nb_bomb_around = 0
    for _ in range(len(grid)):
        # print('y:', y)
        x = 0
        for _ in range(len(grid)):
            # print('x:', x)
            # print("grid[y][x]:", grid[y][x])
            if check_bomb(grid[y][x]) == False:
                x_bomb = x
                y_bomb = y
                nb_bomb_around = count_bomb_around(grid=grid, x=x_bomb, y=y_bomb)
                # print("nb_bomb_around:", nb_bomb_around)
                grid[y_bomb].pop(x_bomb)
                grid[y_bomb].insert(x_bomb, {'content': nb_bomb_around, 'state': hidden_cell})
                # print("Bomb!\nx:",x," y:",y)
                nb_bomb_around = 0
            x += 1
        # incrémenter la position y
        y += 1

    return grid

# Todo: Configurer la grille avec les bombes et nombres
def configure_grid(size):
    grid = make_empty_ms_grid(size)
    # print("grid made:", grid)
    place_bombs(grid)
    # print("grid bombed:", grid)
    place_numbers(grid)
    # print("grid numbered:", grid)
    return grid

# Afficher la grille pour tester
def display_cells_test(cells):
    for items in cells:
        for item in items:
            # print(" ! ",find_value(dico=item, key='content'), end= "")
            if(item.get("state") == "hidden"):
                print(" ◻️ ", end= "")
            else:
                if(item.get("content") == bomb_value):
                    print("  *  ", end='')
                else:
                    print(" ",item.get("content")," ", end='') 
        print()
    # print(cells)

# check_bomb contrôle la présence d'une bombe)
def check_bomb(dico):
    try:
        true_false = False

        if dico.get("content") == bomb_value:
                        true_false = True
    finally:
        return true_false

# find_value recherche la valeur par clé dans le dictionnaire
def find_value(dico, key):
    try:
        return dico[key]
    except KeyError:
        return("None")

# update_value met à jour la valeur d'une clé dans le dictionnaire
def update_value(dico, key, val):
    try:
        dico[key] = val
        return dico
    except KeyError:
        print("update_value: Error!")
        dico.update({key, val})
        return dico

# launch est une boucle de lanceur de test
def launch():
    i = 1
    while i > 0:
        size = input ("Please, input size or q to quit? ")
        if size == 'q' or size is not int:
            print("spring break")
            break
        elif size > 0:      
            print("let's hunt the Bomb")
            size = force_min_size(int(grid_size(int(size))))
            print("size", size)
        else:
            print("Size must be a positive integer... ")
    return size

try:
    print("hello, World!")
    if sys.argv[1]:
        size = int(sys.argv[1])
except Exception:
    print("You must add command line argument: size of the grid!")
    size = int(launch())
finally:
    print("finally-size:", size)
    grid = configure_grid(int(size))
    print("grid configured")
    display_cells_test(grid)       

