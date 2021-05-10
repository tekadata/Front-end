# 34567 101234567 201234567 3012345678 4012345678 501234567 601234567 701234567
# Write a function named conditional_sum that takes a list of integers and a \
# list of booleans as arguments. Both lists will contain the same number of \
# elements. The function will return the sum of all numbers \
# (from the 1st list) that are at the same index as a True in the 2nd list.


def conditional_sum(lov_int, lov_boo):
    sum_int = 0
    for itm in range(len(lov_boo)):
        # conditional_sum.py:11:25: E712 comparison to True should be 'if cond is True:' or 'if cond:'
        if lov_boo[itm]:
            sum_int += lov_int[itm]
    return sum_int


# print("Call/Result/Except:")
# print("[10, 2, 3, 4], [True, False, False, True]")
# print(conditional_sum([10, 2, 3, 4], [True, False, False, True]))
# print(14)
