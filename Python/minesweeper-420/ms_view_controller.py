import pyglet
import sys
from ms_view_model import *


# 1 Recuper la valeur du parametre
# 2 Configurer le dictionnaire 
#   - Ajouter les bombes
#   - Ajouter les nombres autours
# 3 Afficher 


try:
    if sys.argv[1]:
        size = int(sys.argv[1])
except Exception:
    print("You must add command line argument: size of the grid!")
    size = 3
finally:
    print("finally-size:", size)


display = pyglet.canvas.get_display()
screen = display.get_default_screen()
config = screen.get_best_config()


# Todo: Creer la windows en fonction de la largeur dynamique
width_height = screen_size(5)
window = pyglet.window.Window(width_height, width_height, config=config)


# Todo: Afficher la grille dans un premiers temps avec les chiffres et bombes
# Todo: Dans un deuxième temps avec les caractères carrée gris(equivalent state hidden) 
def display_cells(grid):
    xlabel = 0
    ylabel = 0
    for cells in grid:
        xlabel = 0
        for cell in cells:
            content = cell_content(cell.get("content"), cell.get("state"))
            pyglet.text.Label(content, x=xlabel, y=ylabel).draw()
            xlabel += space
        ylabel += space


@window.event
def on_draw():
    display_cells(configure_grid(5))


@window.event
def on_mouse_release(x, y, button,modifiers):
    if(button == 1):
        print("1")
    else:
        print("0")


pyglet.app.run()