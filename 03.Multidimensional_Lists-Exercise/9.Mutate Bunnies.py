rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = input()

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 'P':
            player_pos = [i, j]

cur_row = player_pos[0]
cur_col = player_pos[1]
is_won = False
is_dead = False
bunny_row_movement = [0, 0, -1, 1]
bunny_col_movement = [-1, 1, 0, 0]

for command in commands:
    if is_won:
        break
    if is_dead:
        break

    if command == 'L':
        step = [0, -1]
    elif command == 'R':
        step = [0, +1]
    elif command == 'U':
        step = [-1, 0]
    elif command == 'D':
        step = [+1, 0]

    matrix[cur_row][cur_col] = '.'

    if not 0 <= cur_row + step[0] < rows or not 0 <= cur_col + step[1] < cols:
        is_won = True
    else:
        to_move = matrix[cur_row + step[0]][cur_col + step[1]]

        if to_move == 'B':
            is_dead = True

        elif to_move == '.':
           if 0 <= cur_row + step[0] < rows and  0 <= cur_col + step[1] < cols:
                matrix[cur_row + step[0]][cur_col + step[1]] = 'P'

        cur_row = cur_row + step[0]
        cur_col = cur_col + step[1]

    to_mutate = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'B':
                for b in range(4):
                    current_bunny_pos = [i + bunny_row_movement[b], j+ bunny_col_movement[b]]
                    if 0 <= current_bunny_pos[0] < rows and 0 <= current_bunny_pos[1] < cols:
                        tuple_position = current_bunny_pos[0], current_bunny_pos[1]
                        if tuple_position not in to_mutate and to_mutate != 'B':
                            to_mutate.append(tuple_position)

    for k in range(len(to_mutate)):
        mutate_row = to_mutate[k][0]
        mutate_col = to_mutate[k][1]
        if matrix[mutate_row][mutate_col] == 'P':
            is_dead = True
        matrix[mutate_row][mutate_col] = 'B'

for row in matrix:
    print(''.join(row))

if is_won:
    print(f'won: {cur_row} {cur_col}')

if is_dead:
    print(f'dead: {cur_row} {cur_col}')

