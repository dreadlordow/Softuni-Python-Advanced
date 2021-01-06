n = int(input())
bomb_number = int(input())
bombs_positions = []
for _ in range(bomb_number):
    r, c = input().split(', ')
    r = r.strip('(')
    r = r.strip(',')
    c = c.strip(')')
    bombs_positions.append((int(r), int(c)))


matrix = []

for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)

for positions in bombs_positions:
    if 0 <= positions[0] < n and 0 <= positions[1] < n:
        matrix[positions[0]][positions[1]] = '*'

row_to_check = [0, 0, -1, 1, -1, -1, 1, 1]
col_to_check = [-1, 1, 0, 0, -1, 1, -1, 1]

for row in range(n):
    for col in range(n):
        if matrix[row][col] != '*':
            for i in range(8):
                if 0 <= row + row_to_check[i] < n and 0 <= col + col_to_check[i] < n:
                    if matrix[row + row_to_check[i]][col + col_to_check[i]] == '*':
                        matrix[row][col] += 1

print('\n'.join([' '.join(map(str,row)) for row in matrix]))