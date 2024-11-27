def study_of_algorithms(n, a, b, mood):
    algorithms = [(i + 1, a[i], b[i]) for i in range(n)]
    interest_sorted = sorted(algorithms, key=lambda x: (-x[1], -x[2], x[0]))
    usefulness_sorted = sorted(algorithms, key=lambda x: (-x[2], -x[1], x[0]))

    interest_index = 0
    usefulness_index = 0
    studied = set()
    result = []

    for mood_today in mood:
        if mood_today == 1:
            while usefulness_index < n and usefulness_sorted[usefulness_index][0] in studied:
                usefulness_index += 1
            current_algorithm = usefulness_sorted[usefulness_index]
            usefulness_index += 1
        else:
            while interest_index < n and interest_sorted[interest_index][0] in studied:
                interest_index += 1
            current_algorithm = interest_sorted[interest_index]
            interest_index += 1
        studied.add(current_algorithm[0])
        result.append(current_algorithm[0])
    return result

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mood = list(map(int, input().split()))
print(*study_of_algorithms(n, a, b, mood))
