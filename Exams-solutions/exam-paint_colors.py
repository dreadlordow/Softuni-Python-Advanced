from _collections import deque

string = deque(input().split())

main_colors = ['red','yellow','blue']
secondary_colors = ['orange','purple','green']
colors_list = []
while string:
    if len(string) == 1:
        last_color = string.pop()
        if last_color in main_colors or last_color in secondary_colors:
            colors_list.append(last_color)
            break
        else:
            break
    if string:
        first = string.popleft()
        second = string.pop()
        result = first+second
        result2 = second+first

    if result  in main_colors or result in secondary_colors :
        colors_list.append(result)
    elif result2 in main_colors or result2 in secondary_colors:
        colors_list.append(result2)

    else:
        first = first [0:len(first)-1]
        second = second [0:len(second)-1]
        string.insert(len(string)//2,first)
        string.insert(len(string) // 2, second)
        if "" in string:
            string.remove("")

if 'orange' in colors_list:
    if not 'red' in colors_list or not 'yellow' in colors_list:
        colors_list.remove('orange')
if 'purple' in colors_list:
    if not 'red' in colors_list or not 'blue' in colors_list:
        colors_list.remove('purple')
if 'green' in colors_list:
    if not 'yellow' in colors_list or not 'blue' in colors_list:
        colors_list.remove('green')

print(colors_list)