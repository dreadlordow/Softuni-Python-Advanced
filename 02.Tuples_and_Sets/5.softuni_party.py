n = int(input())

guests = set()
attended = set()
for _ in range(n):
    num = input()
    guests.add(num)

while True:
    line = input()
    if line == 'END':
        break
    attended.add(line)

unattended = guests - attended
print(len(unattended))
print('\n'.join(sorted(unattended)))
