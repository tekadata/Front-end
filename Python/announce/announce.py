def announce(myTuple):
    if myTuple:
        # print a message with all player names.
        print("The contenders today are: ", end='')
        iTuple = len(myTuple)
        print(iTuple)
        for i in range(iTuple):
            print(myTuple[i], end='')
            print(', ', end='')
    else:
        # the tuple is empty,
        print("Nobody will fight today!")
    print()
