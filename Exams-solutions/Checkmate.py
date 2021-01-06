n = 8
matrix = [input().split() for _ in range(n)]
kings_coordinates = []
steps = (
    [-1, 0],
    [+1, 0],
    [0, -1],
     [0, +1],
    [-1, -1],
    [-1, +1],
    [+1, -1],
    [+1, +1]
)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'Q':
            for step in steps:
                queen_row = i
                queen_col = j
                row_to_go = step[0]
                col_to_go = step[1]
                row = row_to_go + i
                col = col_to_go + j

                while True:
                    if row < 0 or col < 0 or row >= n or col >= n:
                        break
                    to_move = matrix[row][col]
                    if to_move == 'K':
                        kings_coordinates.append([queen_row, queen_col])
                    elif to_move == '.':
                        pass
                    elif to_move == 'Q':
                        break
                    row += step[0]
                    col += step[1]
if len(kings_coordinates) == 0:
    print('The king is safe!')
else:
    for cord in kings_coordinates:
        print(cord)
