from collections import Counter
with open("7.txt", "r") as f:
    crabs = Counter(map(int, f.readline().split(",")))

fuel = 0
while len(crabs) > 1:
    center = 0
    for pos, count in crabs.items():
        center += pos * count
    center /= sum(crabs.values())
    farthest = center
    for pos in crabs.keys():
        if abs(pos-center) > abs(farthest-center):
            farthest = pos
    move = int((center-farthest) / abs(center-farthest))
    count = crabs[farthest]
    del crabs[farthest]
    crabs[farthest+move] += count
    fuel += count
print(fuel)