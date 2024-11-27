def triple_product_sum(n, a):
    mod = 1000000007
    total_sum = sum(a) % mod
    result = 0
    L = 0
    
    for j in range(n):
        R = (total_sum - L - a[j]) % mod 
        result = (result + a[j] * L % mod * R % mod) % mod
        L = (L + a[j]) % mod

    return result

n = int(input())
a = list(map(int, input().split()))
print(triple_product_sum(n, a))
