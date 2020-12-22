from _collections import deque

price_of_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
money_spent = 0

while bullets and locks:
    for i in range(gun_barrel_size):
        if not bullets or not locks:
            break
        current_bullet = bullets.pop()

        current_lock = locks.popleft()
        money_spent += price_of_bullet
        if current_bullet <= current_lock:
            print(f'Bang!')
        else:
            locks.appendleft(current_lock)
            print('Ping!')
        if i == gun_barrel_size - 1 and bullets:
            print('Reloading!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f'{len(bullets)} bullets left. Earned ${intelligence_value - money_spent}')