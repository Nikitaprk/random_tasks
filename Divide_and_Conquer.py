# Given a mixed array of number and string representations of integers, add up the string integers and subtract this
# from the total of the non-string integers.


def div_con(x):
    lst_str = []
    lst_int = []
    for i in x:
        if type(i) == str:
            i = int(i)
            lst_str.append(i)
        elif type(i) == int:
            lst_int.append(i)

    return (sum(lst_int) - sum(lst_str))


print(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]))
print(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))
print(div_con(['1', '5', '8', 8, 9, 9, 2, '3']))
print(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))