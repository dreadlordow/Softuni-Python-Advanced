stack = list(input())

reversed = ''
while len(stack) > 0:
    item = stack.pop()
    reversed+=item
print(reversed)