def min_days_to_complete_tasks(n, k, tasks):
    tasks.sort()
    
    l = r = 0
    days = 0
    
    while l < n:
        while r < n and tasks[r] - tasks[l] <= k:
            r += 1
        days = max(days, r - l)
        l += 1
    return days 

n, k = map(int, input().split())
tasks = list(map(int, input().split()))
print(min_days_to_complete_tasks(n, k, tasks))
