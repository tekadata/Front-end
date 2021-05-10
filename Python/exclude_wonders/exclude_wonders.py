def exclude_wonders(lArgs):
    if len(lArgs) > 1:
        lArgs.pop()
        lArgs.remove(lArgs[0])
    return lArgs
