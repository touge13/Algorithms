def find_stopping_indices(n, a, m, k, x_list):
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
    
    return [stop_indices[x - 1] + 1 for x in x_list]

n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x_list = list(map(int, input().split()))
print(*find_stopping_indices(n, a, m, k, x_list))
