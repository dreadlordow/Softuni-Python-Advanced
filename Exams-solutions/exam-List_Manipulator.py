def list_manipulator(*args):
    numbers_list, command, position, *numbers = args

    if command == 'add' and position == 'beginning':
        if len(numbers) > 0:
            for i,el in enumerate(numbers):
                numbers_list.insert(i, el)
        return numbers_list

    elif command == 'add' and position == 'end':
        if len(numbers) > 0:
            for n in numbers:
                numbers_list.append(n)
        return numbers_list

    elif command == 'remove' and position == 'beginning':

        if len(numbers) > 0:
            for i in range(numbers[0]):
                del numbers_list[0]
        else:
            del numbers_list[0]
        return numbers_list

    elif command == 'remove' and position == 'end':
        if len(numbers) > 0:
            for i in range(numbers[0]):
                numbers_list.pop()
        else:
            numbers_list.pop()
        return numbers_list

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

