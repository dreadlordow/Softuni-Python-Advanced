n = int(input())
parking = set()

for _ in range(n):
    direction, plate = input().split(', ')
    if direction == 'IN':
        parking.add(plate)
    elif direction == 'OUT':
        if plate in parking:
            parking.remove(plate)
if parking:
    print('\n'.join(parking))
else:
    print(f'Parking Lot is Empty')
