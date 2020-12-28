n = int(input())
matrix = [list(input()) for _ in range(n)]
searched = input()
is_occured = False
for i, row in enumerate(matrix):
    for j,value in enumerate(row):
        if value == searched:
            print(f'{(i, j)}')
            is_occured = True
            break
    if is_occured:
        break
if not is_occured:
    print(f'{searched} does not occur in the matrix')