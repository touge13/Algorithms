import random

def find_minimal_clothes_v1(A, B, C, D):
    ...
def find_minimal_clothes_v2(A, B, C, D):
    ...

for _ in range(100): 
    A = random.randint(0, 10)
    B = random.randint(0, 10)
    C = random.randint(0, 10)
    D = random.randint(0, 10)
    
    result_v1 = find_minimal_clothes_v1(A, B, C, D)
    result_v2 = find_minimal_clothes_v2(A, B, C, D)
    
    if result_v1 != result_v2:
        print(f"Test failed for A={A}, B={B}, C={C}, D={D}:")
        print(f"Result v1: {result_v1}, Result v2: {result_v2}")
        print("----------")
print("the end")
