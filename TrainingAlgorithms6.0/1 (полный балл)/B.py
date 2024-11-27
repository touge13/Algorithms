def find_minimal_clothes(A, B, C, D):
    if A == 0:
        return 1, C + 1
    elif B == 0:
        return 1, D + 1
    elif C == 0:
        return A + 1, 1
    elif D == 0:
        return B + 1, 1
    
    min_sum = float("inf")
    M, N = 0, 0
    
    if A > B:
        if min_sum > A + 2:
            min_sum = A + 2
            M, N = A + 1, 1
    else:
        if min_sum > B + 2:
            min_sum = B + 2
            M, N = B + 1, 1
    
    if C > D:
        if min_sum > C + 2:
            min_sum = C + 2
            M, N = 1, C + 1
    else:
        if min_sum > D + 2:
            min_sum = D + 2
            M, N = 1, D + 1
    
    if A + C > B + D:
        if min_sum > B + D + 2:
            min_sum = B + D + 2
            M, N = B + 1, D + 1
    else:
        if min_sum > A + C + 2:
            min_sum = A + C + 2
            M, N = A + 1, C + 1
    
    return M, N

A = int(input()) 
B = int(input()) 
C = int(input()) 
D = int(input()) 
M, N = find_minimal_clothes(A, B, C, D)
print(M, N)
