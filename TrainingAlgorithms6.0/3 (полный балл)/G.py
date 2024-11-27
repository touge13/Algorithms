from collections import deque

def compute_total_time_in_queue(n, b, a):
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

n, b = map(int, input().split())
a = list(map(int, input().split()))
print(compute_total_time_in_queue(n, b, a))
