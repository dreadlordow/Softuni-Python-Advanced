def is_valid(pos,size):
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size


def get_killed_knights(row, col, size, matrix):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]
        if is_valid(current_pos, size) and matrix[current_pos[0]][current_pos[1]] == 'K':
            killed_knights += 1
    return killed_knights


n = int(input())
matrix = [[x for x in input()] for _ in range(n)]
total_kills = 0
while True :
    most_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'K':
                killed_knights = get_killed_knights(row, col, n, matrix)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row,col]

    if most_kills == 0:
        break

    row_to_kill = to_kill[0]
    col_to_kill = to_kill[1]
    matrix[row_to_kill][col_to_kill] = '0'
    total_kills += 1

print(total_kills)
