import random

# O(n + m)
def v1(n, a, m, k, x_list):
    stop_indices = [0] * n
    same_value_count = [0] * n
    min_index_for_count = {0 : 0}
    last_switch_index = 0

    for i in range(1, n):
        if a[i - 1] == a[i]:
            same_value_count[i] = same_value_count[i - 1] + 1
            min_index_for_count[same_value_count[i]] = i
        else:
            same_value_count[i] = same_value_count[i - 1]

    for i in range(1, n):
        if a[i - 1] > a[i]:
            last_switch_index = i
        if same_value_count[i] >= k:
            stop_indices[i] = max(last_switch_index, min_index_for_count[same_value_count[i] - k])
        else:
            stop_indices[i] = last_switch_index
    
    result = [stop_indices[x - 1] + 1 for x in x_list]
    return result

# O(n * m)
def v2(n, a, m, k, x_list):
    results = []
    for start in x_list:
        current = start - 1
        remaining_moves = k
        while current > 0:
            if a[current - 1] <= a[current]:
                current -= 1
                if a[current] == a[current + 1]:
                    remaining_moves -= 1
                    if remaining_moves < 0:
                        current += 1
                        break
            else:
                break
        results.append(current + 1)
    return results

print("Started")
for _ in range(25000): 
    n = random.randint(1, 1000) 
    a = [random.randint(0, 1000) for _ in range(n)]
    k = random.randint(0, 1000)
    m = random.randint(1, 1000) 
    x_list = [random.randint(1, n) for _ in range(m)]

    result_v1 = v1(n,a,m,k,x_list)
    result_v2 = v2(n,a,m,k,x_list)
    
    if result_v1 != result_v2:
        print(f"Result v1: {result_v1}, Result v2: {result_v2}")
        print("----------")
print("Finished")
