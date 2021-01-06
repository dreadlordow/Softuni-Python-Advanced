n = int(input())
matrix = [list(input().split()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'B':
            row, col = i, j

commands = ['up', 'down', 'left', 'right']

best_eggs = -999999999999
best_direction = ''
coordinates_list = []
command_counter = 0
best_coordinates = []

for command in commands:
    coordinates_list.append([])
    if command == 'up':
        step = [-1, 0]
    elif command == 'down':
        step = [+1, 0]
    elif command == 'left':
        step = [0, -1]
    elif command == 'right':
        step = [0, +1]

    bunny_row = row
    bunny_col = col
    eggs = 0

    while True:
        if 0 <= bunny_row + step[0] < n and 0 <= bunny_col + step[1] < n:
            to_move = matrix[bunny_row + step[0]][bunny_col + step[1]]

            if matrix[bunny_row + step[0]][bunny_col+step[1]] != 'X':
                coordinates_list[command_counter].append([bunny_row + step[0], bunny_col + step[1]])

            if to_move != 'X':
                eggs += int(to_move)

            elif to_move == 'X':
                break

            if eggs > best_eggs:
                best_coordinates.clear()
                best_coordinates.append(coordinates_list[command_counter])
                best_eggs = eggs
                best_direction = command
            bunny_row += step[0]
            bunny_col += step[1]

        else:
            break
    command_counter += 1

print(best_direction)
for cord in best_coordinates:
    for c in cord:
        print(c)
print(best_eggs)
