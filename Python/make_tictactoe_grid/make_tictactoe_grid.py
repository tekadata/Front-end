# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named make_tictactoe_grid that takes no arguments and \
# returns a 3*3 grid filled with "O" and "X" strings.
# The grid will have Os and Xs distributed as follow:
# O | X | O
# O | O | X
# X | O | X


# def make_tictactoe_grid():
#     lov_1st_row = ["O", "X", "O"]
#     lov_2nd_row = ["O", "O", "X"]
#     lov_3rd_row = ["X", "O", "X"]
#     grd_3X3_tictactoe =[lov_1st_row, lov_2nd_row, lov_3rd_row]
#     for ele_row in grd_3X3_tictactoe:
#         for ind_ele_col in range(len(ele_row)):
#             print(ele_row[ind_ele_col],end='')
#             if ind_ele_col < len(ele_row) - 1:
#                 print(' | ',end='')
#         print()


# def make_tictactoe_grid_beta():
#     str_1st_row = "O | X | O"
#     lov_2nd_row = "O | O | X"
#     lov_3rd_row = "X | O | X"
#     print(str_1st_row)
#     print(lov_2nd_row)
#     print(lov_3rd_row)


def make_tictactoe_grid():
    return [["O", "X", "O"], ["O", "O", "X"], ["X", "O", "X"]]


# print(make_tictactoe_grid())
# print()
# make_tictactoe_grid_beta()
# print()
# make_tictactoe_grid_very_beta()
