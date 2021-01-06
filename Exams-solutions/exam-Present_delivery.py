m = int(input())
n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]

directions = {'up': (-1, 0), 'down': (+1, 0), 'left': (0, -1), 'right': (0, +1)}
nice_kids = 0
kids = nice_kids
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            santa_pos = [i, j]
        elif matrix[i][j] == 'V':
            nice_kids += 1
kids = nice_kids
is_ran_out = False
while True:
    command = input()
    if command == 'Christmas morning':
        break

    r = santa_pos[0] + directions[command][0]
    c = santa_pos[1] + directions[command][1]
    to_move = matrix[r][c]
    if to_move != 'C':
        if to_move == 'V':
            m -= 1
            nice_kids -= 1
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        matrix[r][c] = 'S'
        santa_pos[0] = r
        santa_pos[1] = c
        if m == 0:
            if nice_kids > 0:
                print('Santa ran out of presents!')
            break
    elif to_move == 'C':
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        matrix[r][c] = 'S'
        santa_pos[0] = r
        santa_pos[1] = c
        for direction in directions:
            row_to_move = santa_pos[0] + directions[direction][0]
            col_to_move = santa_pos[1] + directions[direction][1]
            to_move = matrix[row_to_move][col_to_move]
            if to_move == 'V':
                m -= 1
                nice_kids -= 1
            elif to_move == 'X':
                m -= 1
            matrix[row_to_move][col_to_move] = '-'
            if m == 0:
                if nice_kids > 0 :
                    print('Santa ran out of presents!')
                is_ran_out = True
                break
        if is_ran_out:
            break

print('\n'.join([' '.join(map(str,row)) for row in matrix]))
if nice_kids == 0:
    print(f'Good job, Santa! {kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids} nice kid/s.')