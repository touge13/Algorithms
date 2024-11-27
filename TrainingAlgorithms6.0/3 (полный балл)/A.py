def validBrackets(brackets):
    stack = []
    d = {"(":")", "[":"]", "{":"}"}
    
    for b in brackets:
        if b in d:
            stack.append(b)
        elif len(stack) == 0 or b != d[stack.pop()]:
            return "no"
    
    if stack:
        return "no"
    else:
        return "yes"
            
brackets = input()
print(validBrackets(brackets))