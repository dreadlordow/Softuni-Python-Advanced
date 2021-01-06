def even_odd(*args):
    command = args[-1]
    args = args[: -1]
    if command == 'even':
        return list(filter(lambda x: x % 2 == 0,args))
    else:
        return (list(filter(lambda x: x % 2 != 0 , args)))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))