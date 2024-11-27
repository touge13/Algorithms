def nearest_smaller_right(n, nums):
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            result[stack.pop()] = i
        stack.append(i)
    return result

n = int(input())
nums = list(map(int, input().split()))
print(*nearest_smaller_right(n, nums))
