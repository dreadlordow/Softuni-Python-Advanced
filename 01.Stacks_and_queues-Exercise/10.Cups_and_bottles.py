from collections import deque

cups_capacities = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]
wasted_water = 0

while cups_capacities and bottles:
    current_cup = cups_capacities.popleft()
    current_bottle = bottles.pop()

    if current_bottle > current_cup:
        wasted_water += (current_bottle-current_cup)
    elif current_cup > current_bottle:
        current_cup -= current_bottle
        cups_capacities.appendleft(current_cup)

if bottles:
    print(f'Bottles: {" ".join([str(x) for x in bottles])}')
if cups_capacities:
    print(f'Cups: {" ".join([str(x) for x in cups_capacities])}')
print(f'Wasted litters of water: {wasted_water}')