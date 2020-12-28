n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
first_sum = 0
for i in range(n):
    sum_1 = matrix[i][i]
    first_sum += sum_1

second_sum = 0

for j in range(n):
    sum_2 = matrix[j][(n-1)-j]
    second_sum += sum_2
print(abs(first_sum-second_sum))
'''
4
11 2 4 5
4 5 6 5
10 8 -12 5
1 2 3 5
'''
