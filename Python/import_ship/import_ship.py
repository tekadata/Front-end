import sys
from ship import navigate
from spaceship import fly

# Importer le module sys(tem)
# navigate()
# fly()
if sys.argv[1] == 'fly':
    fly(sys.argv[2])
elif sys.argv[1] == 'navigate':
    navigate(sys.argv[2])
