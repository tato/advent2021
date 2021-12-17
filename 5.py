from collections import defaultdict
with open("5.txt", "r") as f:
    lines = [[[int(x) for x in point.split(",") ]for point in line.split("->")] for line in f.readlines()]

points = defaultdict(int)
straight_points = defaultdict(int)
for [[x1, y1], [x2, y2]] in lines:
    dx = max(min(x2-x1, 1), -1)
    dy = max(min(y2-y1, 1), -1)
    x, y = x1, y1
    while x != x2 or y != y2:
        points[(x,y)] += 1
        if x1 == x2 or y1 == y2:
            straight_points[(x,y)] += 1
        x += dx
        y += dy
    points[(x,y)] += 1
    if x1 == x2 or y1 == y2:
        straight_points[(x,y)] += 1
print(len([0 for v in straight_points.values() if v > 1]))
print(len([0 for v in points.values() if v > 1]))