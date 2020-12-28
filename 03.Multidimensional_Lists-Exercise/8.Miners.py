def get_direction(command):
    if command == 'up':
        step = [-1, 0]
    elif command == 'down':
        step = [+1, 0]
    elif command == 'left':
        step = [0, -1]
    elif command == 'right':
        step = [0, +1]

    return step


def get_miner_movement(current_position, step, matrix, n, r, c):
    counter = 0
    if  0 <= r + step[0] < n and  0 <=  c + step[1] < n:
        rtg = r + step[0]
        ctg = c + step[1]
    else:
        rtg = r
        ctg = c

    return  rtg, ctg

n = int(input())
commands = input().split()
matrix =[[x for x in input().split()] for _ in range(n)]

pos = []
coal_count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 's':
            pos = i, j
        if matrix[i][j] == 'c':
            coal_count += 1
r = pos[0]
c = pos[1]
start = matrix[r][c]
current_position = start
coal_counter = 0
is_ended = True
for command in commands:
    step = get_direction(command)
    current_position = get_miner_movement(current_position, step, matrix, n, r, c)
    if not 0 <= current_position[0] < n and not 0 <= current_position[1] < n:
        continue
    r = current_position[0]
    c = current_position[1]
    position = matrix[r][c]
    if position == 'c':
        coal_counter += 1
        matrix[r][c] = "*"
        if coal_counter == coal_count:
            print(f'You collected all coals!', end=' ')
            print(f'({r}, {c})')
            is_ended = False
            break
    elif position == 'e':
        print('Game over!', end=' ')
        print(f'({r}, {c})')
        is_ended = False
        break

if is_ended:
    print(f'{coal_count - coal_counter} coals left. ({r}, {c})')