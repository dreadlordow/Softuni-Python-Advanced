n = int(input())
matrix = [[int(x) for x in input().split(', ')]for _ in range(n)]
f = [matrix[i][i] for i in range(n)]
s = sum(f)
sec = [matrix[n - 1 - i][i] for i in range(n-1, -1, -1)]
sm = sum(sec)
print(f'First diagonal: {", ".join([str(x) for x in f])}. Sum: {s}')
print(f'Second diagonal: {", ".join([str(x) for x in sec])}. Sum: {sm}')
