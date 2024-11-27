def max_length_substring(n, c, s):
    left = 0
    count_a = 0
    count_b = 0
    count_ab = 0
    max_length = 0
    
    for right in range(n):
        if s[right] == 'a':
            count_a += 1
        elif s[right] == 'b':
            count_b += 1
            count_ab += count_a
        while count_ab > c:
            if s[left] == 'a':
                count_a -= 1
                count_ab -= count_b
            elif s[left] == 'b':
                count_b -= 1
            left += 1
            if left > right:
                break
        max_length = max(max_length, right - left + 1)
    return max_length

n, c = map(int, input().split())
s = input().strip()
print(max_length_substring(n, c, s))
