n = int(input())

stack = []

for _ in range(n):
    query = input()
    if query.startswith('1'):
        stack.append(int(query.split()[1]))
    elif query.startswith('2'):
        if len(stack) > 0:
            stack.pop()
    elif query == '3':
        if len(stack) > 0:
            print(max(stack))
    elif query == '4':
        if len(stack) > 0:
            print(min(stack))

print(', '.join([str(x) for x in stack[::-1]]))