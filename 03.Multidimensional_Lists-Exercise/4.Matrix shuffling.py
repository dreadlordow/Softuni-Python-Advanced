rows, cols = [int(x) for x in input().split()]
matrix = [[str(x) for x in input().split()]for _ in range(rows)]

while True:
    line = input()

    if line == 'END':
        break
    elif len(line.split()) < 5 or len(line.split()) > 5:
        print('Invalid input!')
        continue
    args = line.split()
    command = args[0]
    row_1 = int(args[1])
    col_1 = int(args[2])
    row_2 = int(args[3])
    col_2 = int(args[4])

    if command != 'swap' or row_1 >= rows or col_1 >= cols or row_2 >= rows or col_2 >= cols:
        print('Invalid input!')
        continue
    else:
        matrix[row_1][col_1] , matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        print(('\n'.join([' '.join(map(str, row)) for row in matrix])))

#print((' \n'.join([' '.join(map(str, row)) for row in matrix])))