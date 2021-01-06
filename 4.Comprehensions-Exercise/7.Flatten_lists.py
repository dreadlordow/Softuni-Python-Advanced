line = input()
result = [x.split(' ') for x in line.split('|')[::-1]]
flat_list = []
for sublist in result:
    for item in sublist:
        if item != '':
            flat_list.append(item)
print(' '.join(flat_list))