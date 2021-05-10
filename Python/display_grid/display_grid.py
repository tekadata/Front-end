# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named display_grid that takes a grid (a list of lists) as \
# argument, and prints each element of the grid.
# It will first print all the elements in the first list, then print all the \
# elements in the second list, and so on.
# Each printed element will be followed by a newline.
# display_grid([
#         ["1", "2", "3"],
#         ["a", "b", "c", "d", "e"],
#         [],
#         ["A", "B"],
#     ])
# 1
# 2
# 3
# a
# b
# c
# d
# e
# A
# B


def display_grid(par_lol):
    for ele in par_lol:
        # print(ele)
        for val in ele:
            print(val)


# print("Call")
# print("display_grid(([['1', '2', '3'],['a', 'b', 'c', 'd', 'e'],[],['A\
# ', 'B'],])")
# print("Result")
# display_grid([["1", "2", "3"], ["a", "b", "c", "d", "e"], [], ["A\
# ", "B"], ])
# print("Excpected")
# print("1\n2\n3\na\nb\nc\nd\ne\nA\nB")
