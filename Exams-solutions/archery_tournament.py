def is_valid(index, integers):
    if 0 <= index < len(integers):
        return True


integers = [int(x) for x in input().split('|')]
total_point = 0
while True:
    line = input()
    if line == 'Game over':
        break
    tokens = line.split('@')
    command = tokens[0]

    if command == 'Shoot Left':
        index = int(tokens[1])
        length = int(tokens[2])
        if is_valid(index, integers):
            for i in range(1, length+1):
                if index == 0:
                    index = len(integers)
                index -= 1
            if integers[index] < 5:
                total_point += integers[index]
                integers[index] = 0
            else:
                total_point += 5
                integers[index] -= 5

    elif command == 'Shoot Right':
        index = int(tokens[1])
        length = int(tokens[2])
        if is_valid(index, integers):
            for i in range(1, length+1):
                if index == len(integers)-1:
                    index = -1
                index += 1
            if integers[index] < 5:
                total_point += integers[index]
                integers[index] = 0
            else:
                total_point += 5
                integers[index] -= 5

    elif command == 'Reverse':
        integers = integers[::-1]
print(' - '.join([str(x) for x in integers]))
print(f'Iskren finished the archery tournament with {total_point} points!')