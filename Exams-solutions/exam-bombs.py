from _collections import deque

bomb_effect = deque(int(x) for x in input().split(', '))
bomb_casing = [int(x) for x in input().split(', ')]
bombs_dict = {'Datura Bombs':0, 'Cherry Bombs':0, 'Smoke Decoy Bombs': 0}
i = 0
while len(bomb_casing) > 0 and len(bomb_effect) > 0:
    summ = [x for x in bombs_dict.values() if x >= 3]
    if len(summ) == 3:
        break
    bomb = bomb_effect.popleft()
    current_casing = bomb_casing.pop()

    if bomb + current_casing == 40:
        bombs_dict['Datura Bombs'] += 1
    elif bomb + current_casing == 60:
        bombs_dict['Cherry Bombs'] += 1
    elif bomb + current_casing == 120:
        bombs_dict['Smoke Decoy Bombs'] += 1
    else:
        bomb_effect.appendleft(bomb)
        bomb_casing.append(current_casing-5)

pouch = True
for value in bombs_dict.values():
    if value < 3:
        pouch = False
if pouch:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if len(bomb_effect) == 0:
    print(f'Bomb Effects: empty')
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in list(bomb_effect)])}")

if len(bomb_casing) == 0:
    print(f'Bomb Casings: empty')
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")

sorted_dict = dict(sorted(bombs_dict.items(),key= lambda x:x[0]))

for key,value in sorted_dict.items():
    print(f'{key}: {value}')
