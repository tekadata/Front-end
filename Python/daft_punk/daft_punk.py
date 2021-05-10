def a():
    return "Work it\nMake it\nDo it\nMakes \
us\nHarder\nBetter\nFaster\nStronger"


def b():
    return "\nMore than\nHour\nOur\nNever\nEver\nAfter\nWork is\nOver\n"


def c():
    return "\nWork it\nHarder\nMake it\nBetter\nDo \
it\nFaster\nMakes us\nStronger\nMore \
than\nEver\nHour\nAfter\nHour\nWork is\nNever\nOver"


def daft_punk():
   print(a(), b(), a(), (c() * 3), end="")
   print()
