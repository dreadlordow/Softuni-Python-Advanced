n = int(input())
matrix =  [[int(x) for x in input().split()] for _ in range(n)]

while True:
    line = input()
    if line == 'END':
        break
    args = line.split()
    command = args[0]
    row = int(args[1])
    col = int(args[2])
    value = int(args[3])
    if 0 > row or row >= n or 0 > col or col >= n:
        print(f'Invalid coordinates')
    else:
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value

print('\n'.join([' '.join(map(str,x)) for x in matrix]))
