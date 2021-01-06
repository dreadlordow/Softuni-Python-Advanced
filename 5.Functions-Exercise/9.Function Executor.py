def func_executor(*args):
    list_res = []
    for el in args:
        fn = el[0]
        arg = el[1]
        r = fn(*arg)
        list_res.append(r)

    return list_res


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

