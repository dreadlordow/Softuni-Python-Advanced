rows, cols = [int(x) for x in input().split()]
matrix = [[l for l in input().split()]for _ in range(rows)]

counter = 0
for i in range(rows-1):
    for j in range(cols-1):
        first_el = matrix[i][j]
        second_el = matrix[i][j+1]
        third_el = matrix[i+1][j]
        fourth_el = matrix[i+1][j+1]
        if first_el == second_el == third_el == fourth_el:
            counter += 1
print(counter)

