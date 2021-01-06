d = {k: {} for k in input().split(', ')}

line = input()
while line != 'End':
    args = line.split('-')
    name = args[0]
    item = args[1]
    price = int(args[2])

    if item not in d[name]:
        d[name][item] = price

    line = input()

[print(f'{name} -> Items: {len(d[name].keys())}, '
       f'Cost: {sum(d[name].values())}')
 for name in d.keys()]

