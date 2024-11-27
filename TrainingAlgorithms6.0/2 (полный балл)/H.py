def moving_to_an_open_space(n, room_capacity):
    left_sum = 0
    right_sum = 0
    current_cost = 0
    
    current_cost = sum(room_capacity[i] * i for i in range(n))
    right_sum = sum(room_capacity) - room_capacity[0]
    result = current_cost

    for i in range(1, n):
        left_sum += room_capacity[i - 1]
        current_cost = current_cost - right_sum + left_sum
        right_sum -= room_capacity[i]
        result = min(result, current_cost)
    return result

n = int(input())
room_capacity = list(map(int, input().split()))
print(moving_to_an_open_space(n, room_capacity))
