from _collections import deque
materials_boxes = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

mdict = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
crafted = {}

while materials_boxes and magic_levels:
    box = materials_boxes[-1]
    magic = magic_levels[0]
    result = box * magic
    if box == 0:
        materials_boxes.pop()
        continue
    elif magic == 0:
        magic_levels.popleft()
        continue
    elif magic == box and magic == 0:
        magic_levels.popleft()
        materials_boxes.pop()
        continue
    elif result < 0:
        result = magic + box
        magic_levels.popleft()
        materials_boxes.pop()
        materials_boxes.append(result)
    elif result not in mdict.keys() and result > 0:
        magic_levels.popleft()
        materials_boxes.append(materials_boxes.pop() + 15)
    elif result in mdict.keys():
        magic_levels.popleft()
        materials_boxes.pop()
        toy = mdict[result]
        if toy not in crafted:
            crafted[toy] = 1
            continue
        crafted[toy] += 1
is_done = False
if 'Doll' in crafted.keys() and 'Wooden train' in crafted.keys():
    if crafted['Doll'] >= 1 and crafted['Wooden train'] >= 1:
        is_done = True
if 'Teddy bear' in crafted.keys() and 'Bicycle' in crafted.keys():
    if crafted['Teddy bear'] >= 1 and crafted['Bicycle'] >= 1:
        is_done = True

if is_done:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials_boxes:
    print(f"Materials left: {', '.join([str(x) for x in materials_boxes][::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

crafted = dict(sorted(crafted.items(), key= lambda x: x[0]))
for k, v in crafted.items():
    print(f'{k}: {v}')