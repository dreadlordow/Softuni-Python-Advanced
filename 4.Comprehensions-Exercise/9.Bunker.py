d = {key: [] for key in input().split(', ')}
n = int(input())
total_items = 0
total_quality = 0
for _ in range(n):
    command = input()
    args = command.split(' - ')
    category = args[0]
    item = args[1]
    quantity_and_quality = args[2].split(';')
    quantity = int(quantity_and_quality[0].split(':')[1])
    quality = int(quantity_and_quality[1].split(':')[1])
    total_items += quantity
    total_quality += quality
    if item not in d[category]:
        d[category].append(item)
print(f'Count of items: {total_items}')
print(f'Average quality: {total_quality/len(d.keys()):.2f}')
for key in d.keys():
    print(f"{key} -> ",end='')
    print(', '.join(d[key]))

