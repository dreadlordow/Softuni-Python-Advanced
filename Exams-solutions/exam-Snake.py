n = int(input())
matrix = [list(input()) for _ in range(n)]

burrows = []
are_burrows = False
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            snake_pos = [i, j]
        elif matrix[i][j] == 'B':
            burrows.append((i, j))
            are_burrows = True
if are_burrows:
    first_burrow = matrix[burrows[0][0]][burrows[0][1]]
    second_burrow = matrix[burrows[1][0]][burrows[1][1]]

cur_row = snake_pos[0]
cur_col = snake_pos[1]
food_counter = 0
while True:
    command = input()
    if command == 'left':
        step = [0, -1]
    elif command == 'right':
        step = [0, +1]
    elif command == 'up':
        step = [-1, 0]
    elif command == 'down':
        step = [+1, 0]

    matrix[cur_row][cur_col] = '.'
    move_row = cur_row + step[0]
    move_col = cur_col + step[1]

    if not 0 <= move_row < n or not 0 <= move_col < n:
        print(f'Game over!')
        break
    else:
        to_move = matrix[move_row][move_col]
        if to_move == '*':
            food_counter += 1
            matrix[move_row][move_col] = 'S'
            cur_row = move_row
            cur_col = move_col
            if food_counter >= 10:
                print(f'You won! You fed the snake.')
                break

        elif to_move == '-':
            matrix[move_row][move_col] = 'S'
            cur_row = move_row
            cur_col = move_col

        elif (burrows[0][0], burrows[0][1]) == (move_row, move_col):
            matrix[move_row][move_col] = '.'
            matrix[burrows[1][0]][burrows[1][1]] = 'S'
            cur_row = burrows[1][0]
            cur_col = burrows[1][1]

        elif (burrows[1][0], burrows[1][1]) == (move_row, move_col):
            matrix[move_row][move_col] = '.'
            matrix[burrows[0][0]][burrows[0][1]] = 'S'
            cur_row = burrows[0][0]
            cur_col = burrows[0][1]

print(f'Food eaten: {food_counter}')
for row in matrix:
    print(''.join(row))