def stack_with_sum(n, data):
    stack = []
    
    for i in range(n):
        operation = data[i]
        
        if operation.startswith('+'):
            x = int(operation[1:])
            if stack:
                stack.append((x, stack[-1][1] + x))
            else:
                stack.append((x, x))

        elif operation == '-':
            x, _ = stack.pop()
            print(x)

        elif operation.startswith('?'):
            k = int(operation[1:])
            if k == 0:
                print(0)
                return 
            total_sum = stack[-1][1] - (stack[-k-1][1] if k < len(stack) else 0)
            print(total_sum)

n = int(input())
data = [input().strip() for _ in range(n)]
stack_with_sum(n, data)
