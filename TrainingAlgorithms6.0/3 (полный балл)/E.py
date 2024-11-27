def evaluate_expression(expression):
    def to_rpn(expr):
        output = []
        operators = []
        priority = {'+' : 1, '-' : 1, '*' : 2}
        
        i = 0
        while i < len(expr):
            char = expr[i]
            if char.isdigit() or (char == '-' and (i == 0 or expr[i - 1] in "+-*/(")):
                num = ""
                if char == '-':
                    num += char
                    i += 1
                while i < len(expr) and expr[i].isdigit():
                    num += expr[i]
                    i += 1
                output.append(int(num))
                continue

            elif char in priority:
                while (operators and operators[-1] != '(' and 
                       priority.get(operators[-1], 0) >= priority[char]):
                    output.append(operators.pop())
                operators.append(char)

            elif char == '(':
                operators.append(char)

            elif char == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if not operators:
                    return None
                operators.pop()
            i += 1

        while operators:
            top = operators.pop()
            if top in '()':
                return None
            output.append(top)
        return output

    def calculate_rpn(rpn_expr):
        stack = []
        for token in rpn_expr:
            if isinstance(token, int):
                stack.append(token)
            else:
                if len(stack) < 2:
                    return None
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
        return stack[0] if len(stack) == 1 else None

    if not all(char in "0123456789+-*() " for char in expression):
        return "WRONG"
    
    i = 0
    while i < len(expression) - 1:
        if expression[i].isdigit() and expression[i + 1] == ' ':
            j = i + 2
            while j < len(expression) and expression[j] == ' ':
                j += 1
            if j < len(expression) and expression[j].isdigit():
                return "WRONG"
        i += 1

    expression = expression.replace(" ", "")
    rpn = to_rpn(expression)
    if rpn is None:
        return "WRONG"

    result = calculate_rpn(rpn)
    return result if result is not None else "WRONG"
    
s = input()
print(evaluate_expression(s))