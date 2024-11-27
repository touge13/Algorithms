def closest_direction_to_raft(x1, y1, x2, y2, x, y):
    if x < x1:
        if y < y1:
            return "SW"
        elif y > y2:
            return "NW"
        else:
            return "W"
    elif x > x2:
        if y < y1:
            return "SE"
        elif y > y2:
            return "NE"
        else:
            return "E"
    else:
        if y < y1:
            return "S"
        elif y > y2:
            return "N"

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

print(closest_direction_to_raft(x1, y1, x2, y2, x, y))
