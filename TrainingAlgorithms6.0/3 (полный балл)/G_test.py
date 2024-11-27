from collections import deque

import random

def v1(n, b, a):
    queue = deque()
    total_time = 0

    for i in range(n):
        for _ in range(a[i]):
            queue.append(i)

        served = min(b, len(queue))
        for _ in range(served):
            arrival_time = queue.popleft()
            total_time += (i + 1) - arrival_time

    while queue:
        arrival_time = queue.popleft()
        total_time += n - arrival_time + 1

    return total_time

def v2(n, b, a):
    queue = deque()
    total_time = 0

    for minute, customer_count in enumerate(a):
        queue.append((minute, customer_count))
    
    for current_minute in range(n):
        available_spots = b
        
        while queue and current_minute >= queue[0][0] and available_spots > 0:
            arrival_time, num_customers = queue.popleft()
            served_customers = min(num_customers, available_spots)
            num_customers -= served_customers
            available_spots -= served_customers
            if num_customers > 0:
                queue.appendleft((arrival_time, num_customers))
            total_time += served_customers * (current_minute + 1 - arrival_time)

    while queue:
        arrival_time, num_customers = queue.popleft()
        total_time += num_customers * (n + 1 - arrival_time)
    
    return total_time

print("Started")
total_tests = 1000
for i in range(total_tests): 
    n = random.randint(1, 1000) 
    a = [random.randint(0, 1000) for _ in range(n)]
    k = random.randint(0, 1000)
    
    result_v1 = v1(n, k, a)
    result_v2 = v2(n, k, a)
    
    if result_v1 != result_v2:
        print(f"Result v1: {result_v1}, Result v2: {result_v2}")
        print("----------")

    if (i + 1) % (total_tests // 10) == 0:
        percent_complete = (i + 1) / total_tests * 100
        print(f"Progress: {percent_complete:.2f}%", end="\r")

print("Finished")
