# Основные операции, которые можно производить со стеклом, включают:
# • Добавление элемента в вершину стека (push) - O(1).
# • Удаление элемента из вершины стека (pop) - O(1).
# • Возврат верхнего элемента без его удаления (peek) - O(1).
# • Проверка стека на пустоту (isEmpty) - O(1).

stack = []
q = int(input())
for _ in range(q):
    userInput = list(map(int, input().split()))
    if len(userInput) == 2:
        stack.append(userInput[1])
        print(userInput[1])
    elif len(userInput) == 1:
        stack.pop()
        if stack:
            print(stack[-1])
        else:
            print(-1)
