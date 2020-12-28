from _collections import deque
n, m = [int(x) for x in input().split()]
snake = deque(list(input()))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append('')

for row in range(n):
    for col in range(m):
        current_col = col
        current_char = snake.popleft()
        if row % 2 != 0:
            current_col = m - 1 - col
        matrix[row][current_col] = current_char
        snake.append(current_char)

for row in matrix:
    print(''.join(row))