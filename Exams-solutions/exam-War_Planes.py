def is_valid(number, size):
    return 0 <= number < size


n = int(input())
matrix = [list(input().split()) for _ in range(n)]

directions = {'up': (-1, 0), 'down': (+1, 0), 'left': (0, -1), 'right': (0, +1)}
targets = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'p':
            plane_pos = [i, j]
        elif matrix[i][j] == 't':
            targets += 1
m = int(input())
count_targets = targets
for _ in range(m):
    commands = input().split()
    command = commands[0]
    direction = commands[1]
    count_steps = int(commands[2])

    steps = (directions[direction][0], directions[direction][1])

    if command == 'move':
        row_to_move = plane_pos[0] + steps[0]*count_steps
        col_to_move = plane_pos[1] + steps[1]*count_steps
        if is_valid(row_to_move, n) and is_valid(col_to_move, n):
            to_move = matrix[row_to_move][col_to_move] # MOVING PLANE
            if to_move == '.':
                matrix[plane_pos[0]][plane_pos[1]] = '.'
                matrix[row_to_move][col_to_move] = 'p'
                plane_pos[0] = row_to_move
                plane_pos[1] = col_to_move

    elif command == 'shoot':
        row_to_shoot = plane_pos[0] + steps[0]*count_steps
        col_to_shoot = plane_pos[1] + steps[1]*count_steps
        if is_valid(row_to_shoot, n) and is_valid(col_to_shoot, n):
            to_shoot = matrix[row_to_shoot][col_to_shoot] # MOVING PLANE
            if to_shoot == '.':
                matrix[row_to_shoot][col_to_shoot] = 'x'
            elif to_shoot == 't':
                matrix[row_to_shoot][col_to_shoot] = 'x'
                targets -= 1
                if targets == 0 :
                    print(f'Mission accomplished! All {count_targets} targets destroyed.')
                    break
if targets > 0:
    print(f'Mission failed! {targets} targets left.')
for row in matrix:
    print(' '.join(row))