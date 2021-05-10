def proper_announce(myTuple):
    if myTuple:
        # print a message with all player names.
        print("The contenders today are: ", end='')
        iTuple = len(myTuple)
        print(iTuple)
        for i in range(iTuple):
            print(myTuple[i], end='')
            if iTuple>2:
                print(' and ', end='')
    else:
        # the tuple is empty,
        print("Nobody will fight today!")
    print()


proper_announce(("Arya", "Jon Snow", "Tyrion"))
proper_announce(("Arya", "Jon Snow"))
proper_announce(())
proper_announce(("Jon", "Sansa", "Arya"))
proper_announce(("Night Walker",))
proper_announce(())
