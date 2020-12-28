def is_valid(current_pos, n):
    row = current_pos[0]
    col = current_pos[1]

    return 0 <= row < n and 0 <= col < n


def get_blasted_matrix(row, col, matrix):
    blast_row = [-1, -1, -1, 0, 0, 1, 1, 1]
    blast_col = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        bomb_value = matrix[row][col]
        current_pos = [row + blast_row[i], col + blast_col[i]]
        if is_valid(current_pos, n) and matrix[current_pos[0]][current_pos[1]] > 0:
            matrix[current_pos[0]][current_pos[1]] -= bomb_value
    matrix[row][col] = 0
    return matrix


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs_input = input().split()



for bombs in bombs_input:
    bomb_location = bombs.split(',')
    row = int(bomb_location[0])
    col = int(bomb_location[1])

    if matrix[row][col] > 0:
        get_blasted_matrix(row, col, matrix)
active_sum = 0
counter = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
           active_sum += matrix[i][j]
           counter += 1

print(f'Alive cells: {counter}')
print(f'Sum: {active_sum}')
print(('\n'.join([' '.join(map(str, row)) for row in matrix])))