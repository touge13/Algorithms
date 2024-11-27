from collections import deque

def find_bounds(table, n):
    x1 = y1 = float("inf")
    x2 = y2 = 0
    found = False
    for y in range(n):
        for x in range(n):
            if table[y][x] == "#":
                found = True
                x1 = min(x1, x)
                y1 = min(y1, y)
                x2 = max(x2, x)
                y2 = max(y2, y)
    
    if not found: 
        return None, None, None, None
    return x1, y1, x2, y2

def is_empty_rect(table, x1, y1, x2, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if table[y][x] != ".":
                return False
    return True

def bfs_find_rects(table, start_x, start_y, visited):
    queue = deque([(start_x,start_y)])
    visited.add((start_x, start_y))
    x_min, x_max, y_min, y_max = start_x, start_x, start_y, start_y
    
    while queue:
        x, y = queue.popleft()
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(table[0]) and 0 <= ny < len(table) and (nx, ny) not in visited:
                if table[ny][nx] == ".":
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return x_min, y_min, x_max, y_max

def find_inner_rects(table, x1, y1, x2, y2):
    visited = set()
    inner_rects = []
    
    for y in range(len(table)):
        for x in range(len(table[y])):
            if table[y][x] == "." and (x, y) not in visited:
                x1, y1, x2, y2 = bfs_find_rects(table, x, y, visited)
                if not is_empty_rect(table, x1, y1, x2, y2):
                    return "X"
                inner_rects.append([(x1, y1), (x2, y2)])
    return inner_rects

def recognize_letter(n, table):
    x1, y1, x2, y2 = find_bounds(table, n)

    if x1 is None:
        return "X"

    table = table[y1 : y2 + 1]
    for i in range(len(table)):
        table[i] = table[i][x1 : x2 + 1]
    
    if len(table) == 0 or len(table[0]) == 0:
        return "X"
    
    inner_rects = find_inner_rects(table, x1, y1, x2, y2)
    if inner_rects == "X":
        return "X"

    if len(inner_rects) == 0:
        return "I"
    
    if len(inner_rects) == 1:
        (x3, y3), (x4, y4) = inner_rects[0]
        if 0 < x3 < (len(table[0]) - 1) and 0 < x4 < (len(table[0]) - 1) and 0 < y3 < (len(table) - 1) and 0 < y4 < (len(table) - 1):
            return "O"
        
        elif 0 < x3 and x4 == (len(table[0]) - 1) and 0 < y3 < (len(table) - 1) and 0 < y4 < (len(table) - 1):
            return "C"
        
        elif 0 < x3 and x4 == (len(table[0]) - 1) and y3 < (len(table) - 1) and y3 == 0:
            return "L"

    if len(inner_rects) == 2:
        (x3, y3), (x4, y4) = inner_rects[0]
        (x5, y5), (x6, y6) = inner_rects[1]
        if x3 == x5 and x4 == x6 and 0 < x3 < (len(table[0]) - 1) and  0 < x6 < (len(table[0]) - 1) and y3 == 0 and y6 == (len(table) - 1):
            return "H"
        
        elif 0 < x4 < (len(table[0]) - 1) and x6 == (len(table[0]) - 1) and x3 == x5 and 0 < x3 < (len(table[0]) - 1) and y6 == (len(table) - 1) and 0 < y3 < (len(table) - 1) and 0 < y4 < (len(table) - 1):
            return "P"

    return "X"

n = int(input())
table = [input().strip() for _ in range(n)]
print(recognize_letter(n, table))

# def test_recognize_letter():
#     test_cases = [
#         (4, [
#             ".##.",
#             ".##.",
#             ".##.",
#             "...."
#         ], "I"),
        
#         (5, [
#             "#...#",
#             ".#.#.",
#             "..#..",
#             ".#.#.",
#             "#...#"
#         ], "X"),  # неопределённый символ

#         (3, [
#             "#.#",
#             "#..",
#             "###"
#         ], "X"),  # неопределённый символ

#         (4, [
#             "##..",
#             "##..",
#             "####",
#             "####"
#         ], "L"),

#         (3, [
#             "###",
#             "#..",
#             "###"
#         ], "C"),

#         (3, [
#             "###",
#             "#.#",
#             "###"
#         ], "O"),

#         (3, [
#             "#.#",
#             "###",
#             "#.#"
#         ], "H"),

#         (4, [
#             "#..#",
#             "####",
#             "####",
#             "#.##"
#         ], "X"),  # неопределённый символ

#         (4, [
#             "####",
#             "#.##",
#             "####",
#             "#..."
#         ], "P"),

#         (4, [
#             "####",
#             "#.##",
#             "####",
#             "#..#"
#         ], "X"),  # неопределённый символ

#         (4, [
#             "####",
#             "#...",
#             "####",
#             "#..."
#         ], "X"),

#         (8, [
#             "........",
#             "........",
#             "..##....",
#             "..##....",
#             ".####...",
#             "..##....",
#             "..##....",
#             "........"
#         ], "X"),

#         (4, [
#             "....",
#             "####",
#             "####",
#             "...."
#         ], "I"),

#         (3, [
#             "###",
#             "##.",
#             "##."
#         ], "X"),

#         (3, [
#             "##.",
#             "##.",
#             "###"
#         ], "L"),

#         (10, [
#             "..........",
#             ".#......#.",
#             ".#......#.",
#             ".#......#.",
#             ".########.",
#             ".#......#.",
#             ".#......#.",
#             ".#......#.",
#             ".#......#.",
#             ".........."
#         ], "H"),
#         (10, [
#             "..........",
#             "..........",
#             "..........",
#             "..........",
#             "..........",
#             "..........",
#             "..........",
#             "..........",
#             "..........",
#             ".........."
#         ], "X")
#     ]
    
#     for i, (n, table, expected) in enumerate(test_cases, 1):
#         result = recognize_letter(n, table)
#         assert result == expected, f"Test {i} failed: expected {expected}, got {result}"

# test_recognize_letter()
