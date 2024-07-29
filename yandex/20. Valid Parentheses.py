class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '{':'}', '[':']'}

        for i in s:
            if i in d: # '(', '{', '['
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i: # последний элемент стека удаляется после этой строки
                return False

        return len(stack) == 0

#({[][]})()
#stack: ({[
#i: ]
#stack: ({
#stack: ({[
#i: ]
#stack: ({
#i: }
#stack: (
# ...