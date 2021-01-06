n, m = [int(x) for x in input().split(' ')]
matrix = [[[''] for x in range(m)]for x in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = f'{chr(97+i)}{chr(97 + (i+j) )}{chr(97+i)}'
for row in matrix:
    print(' '.join(row))
