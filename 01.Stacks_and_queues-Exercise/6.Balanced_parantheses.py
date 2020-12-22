parenthesis = input()
stack = []
is_valid = True
for bracket in parenthesis:
    if bracket == '(' or bracket == '{' or bracket == '[':
        stack.append(bracket)
    else:
        if len(stack) == 0:
            is_valid = False
            break
        bracket_to_check = stack.pop()
        if bracket_to_check == '[' and bracket == ']':
            continue

        elif bracket_to_check == '{' and bracket == '}':
            continue

        elif bracket_to_check == '(' and bracket == ')':
            continue
        else:
            is_valid = False
            break
if not is_valid:
    print('NO')
else:
    print('YES')