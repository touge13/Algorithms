from collections import deque

def calculate_crossing_times(N, a, b, rovers):
    queues= {0: deque(sorted(((i, time) for i, direction, time in rovers if direction == 1), key=lambda x: x[1])),
             1: deque(sorted(((i, time) for i, direction, time in rovers if direction == 2), key=lambda x: x[1])),
             2: deque(sorted(((i, time) for i, direction, time in rovers if direction == 3), key=lambda x: x[1])),
             3: deque(sorted(((i, time) for i, direction, time in rovers if direction == 4), key=lambda x: x[1]))
    }
    time = 1
    pass_time = [-1] * N

    while any(queues.values()): 

        ready_cars = {}
        for direction in queues.keys():
            if queues[direction] and queues[direction][0][1] <= time:
                ready_cars[direction] = queues[direction][0]
        
        main_road_cars = {d: car for d, car in ready_cars.items() if d in {a - 1, b - 1}}
        side_road_cars = {d: car for d, car in ready_cars.items() if d not in {a - 1, b - 1}}

        crossing_cars = {}
        for direction, car in main_road_cars.items():
            if (direction - 1) % 4 not in main_road_cars:
                crossing_cars[direction] = car

        for direction, car in side_road_cars.items():
            if (direction - 1) % 4 not in ready_cars and \
               (direction + 1) % 4 not in crossing_cars and \
                not main_road_cars:
                crossing_cars[direction] = car

        for direction in crossing_cars:
            queues[direction].popleft()
            pass_time[crossing_cars[direction][0]] = time

        time += 1
        
    for t in pass_time:
        print(t)

N = int(input())
a, b = map(int, input().split())
rovers = []

for i in range(N):
    d, t = map(int, input().split())
    rovers.append((i, d, t))
    
calculate_crossing_times(N,a,b,rovers)