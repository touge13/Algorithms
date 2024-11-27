def removing_medians(n, nums):
    nums.sort()
    res = []
    r = n // 2      # pointer for even case
    l = n // 2 - 1  # pointer for odd case
    parity = n % 2

    while l >= 0 and r < n:
        if parity == 0:
            res.append(nums[l])
            l -= 1
            parity = 1
        else:
            res.append(nums[r])
            r += 1
            parity = 0
    
    # эти два цикла итерируются один раз, и то только в случае, 
    # если четность массива - нечетна, можно было их разместить 
    # в первом цикле (выше), либо использовать if.
    # В общем, не очень красиво, но оставлю как есть, ибо жмут дедлайны
    while l >= 0:
        res.append(nums[l])
        l -= 1
    
    while r < n:
        res.append(nums[r])
        r += 1

    return res

n = int(input())
nums = list(map(int, input().split()))
print(*removing_medians(n, nums))
