# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named make_none_grid that takes an integer \
# (representing a size) as argument.
# Your function will return a grid (a list of lists) of size by size elements.
# Each element of the grid will be set to None.
# print(make_none_grid(3))
# [[None, None, None], [None, None, None], [None, None, None]]


def make_none_grid(par_size):
    grd_square_none = []
    lov_none = []
    ind_grid = 0
    while ind_grid < par_size:
        ind_list = 0
        while ind_list < par_size:
            lov_none += [None]
            # print('i', ind_list, 'lov[i]', lov_none[ind_list], end='')
            ind_list += 1
        # print()
        # print("lov", lov_none)
        grd_square_none += [lov_none, ]
        # print("grd", grd_square_none)
        # print('i', ind_grid, 'grid[i]', grd_square_none[ind_grid], end='')
        ind_grid += 1
        lov_none = []
        # print()
    return grd_square_none


# print(make_none_grid(3))
# print("Call")
# print("make_none_grid(3)")
# print("Result")
# print(make_none_grid(3))
# print("Excpected")
# print("[[None, None, None], [None, None, None], [None, None, None]]")
