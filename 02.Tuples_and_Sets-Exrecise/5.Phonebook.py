my_dict = {}
is_break = False
while True:
    line = input()
    if not line.isdigit():
        name, number = line.split('-')
        if name not in my_dict:
            my_dict[name] = ''
        my_dict[name] = number

    else:
        n = int(line)
        for _ in range(n):
            user = input()
            if user in my_dict.keys():
                print(f'{user} -> {my_dict[user]}')
            else:
                print(f'Contact {user} does not exist.')
            if _ == n-1:
                is_break = True
                break
    if is_break:
        break



