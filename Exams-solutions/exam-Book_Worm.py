string = input()
n = int(input())

matrix = [[x for x in input()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'P':
            player_pos = [i, j]

directions = {
    'up': [-1, 0],
    'down': [+1, 0],
    'right': [0, +1],
    'left': [0, -1]
}

row = player_pos[0]
col = player_pos[1]
while True:
    line = input()
    if line == 'end':
        break
    steps = directions[line]
    if row + steps[0]< 0 or row + steps[0] >= n or col + steps[1] <0 or col + steps[1] >= n:
        if len(string) > 0:
            string = string[0:-1]

    else:
        rtm = row + steps[0]
        ctm = col + steps[1]
        to_move = matrix[rtm][ctm]
        if to_move.isalpha():
            string += matrix[rtm][ctm]
        matrix[row][col] = '-'
        matrix[rtm][ctm] = 'P'
        row = rtm
        col = ctm
print(string)
for line in matrix:
    print(''.join(line))