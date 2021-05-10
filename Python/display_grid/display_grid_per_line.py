# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named display_grid_per_line that takes a grid of strings as\
# argument. The function will print the grid, sublist by sublist.
# Each sublist will be printed on its own line, with " => " as separation\
# between two elements.


def display_grid_per_line(par_lol_str):
    for sub_lost in par_lol:
        # print(ele)
        for ele in sub_lost:
            print(ele)
            print('=>')


print("Call")
print("display_grid_per_line([['1', '2', '3'],['a', 'b', 'c', 'd', 'e'],[],['A', 'B''],])")
print("Result")
display_grid_per_line([["1", "2", "3"],["a", "b", "c", "d", "e"],[],["A", "B"],])
print("Expected")
print("1 => 2 => 3\na => b => c => d => e\n\nA => B")

