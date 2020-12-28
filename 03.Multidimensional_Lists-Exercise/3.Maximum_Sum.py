from itertools import chain

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

squares = []
for i in range(rows - 2):
    for j in range(cols - 2):
        squares.append((matrix[i][j:j + 3],
                        matrix[i + 1][j:j + 3],
                        matrix[i + 2][j:j + 3]))
best_square = []
square_sum = -33333333333333333333333333333333333333333333

for square in squares:
    if sum(chain(*square)) > square_sum:
        square_sum = sum(chain(*square))
        best_square = square

if best_square:
    print(f'Sum = {square_sum}')
    print(('\n'.join([' '.join(map(str,row)) for row in best_square])))


