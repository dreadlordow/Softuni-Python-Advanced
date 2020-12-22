from _collections import deque

green_time = int(input())
window_time = int(input())
crashed = False
line = input()

cars = deque()
all_cars = []

while line != 'END':
    if line == 'green':
        timer = green_time
        if cars:
            copy = cars.popleft()
            current_car = deque(copy)

            while timer:
                if not current_car:
                    if cars:
                        copy = cars.popleft()
                        current_car = deque(copy)

                    else:
                        break
                current_car.popleft()
                timer -= 1
            if current_car:
                window_timer = window_time
                while window_timer and current_car:
                    current_car.popleft()
                    window_timer -= 1
            if current_car:
                crashed = True
                print(f'A crash happened!')
                print(f'{copy} was hit at {current_car.popleft()}.')
                break

    else:
        cars.append(line)
        all_cars.append(line)
    line = input()
if not crashed:
    print(f'Everyone is safe.')
    print(f'{len(all_cars)-len(cars)} total cars passed the crossroads.')