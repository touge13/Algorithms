from collections import deque

def min_discomfort(n, H, heights, widths):
    chairs = sorted((heights[i], widths[i]) for i in range(n))
    left = 0
    current_width_sum = 0
    min_discomfort = float('inf')
    max_diff_deque = deque()
    
    for right in range(n):
        current_width_sum += chairs[right][1]
        
        if right > 0:
            diff = abs(chairs[right][0] - chairs[right - 1][0])
            while max_diff_deque and max_diff_deque[-1] < diff:
                max_diff_deque.pop()
            max_diff_deque.append(diff)
        
        while current_width_sum >= H:
            current_discomfort = max_diff_deque[0] if max_diff_deque else 0
            min_discomfort = min(min_discomfort, current_discomfort)
            current_width_sum -= chairs[left][1]
            
            if left < right:
                diff_left = abs(chairs[left + 1][0] - chairs[left][0])
                if max_diff_deque and max_diff_deque[0] == diff_left:
                    max_diff_deque.popleft()
            
            left += 1
    return min_discomfort

n, H = map(int, input().split())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))
print(min_discomfort(n, H, heights, widths))
