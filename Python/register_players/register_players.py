def register_players():
    myPlaya = input("Name your first player: ")
    myPlayazTuple = (myPlaya,)
    while myPlaya:
        myPlaya = input("Name another of your players: ")
        if myPlaya:
            myPlayazTuple += (myPlaya,)
    return myPlayazTuple
