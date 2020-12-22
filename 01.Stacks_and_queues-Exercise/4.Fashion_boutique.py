stack = input().split()
capacity = int(input())
value_sum = 0
racks = 1

while len(stack) > 0:
    value_sum += int(stack[-1])
    if value_sum <= capacity:
        stack.pop()

    else:
        racks += 1
        value_sum = 0

print(racks)
