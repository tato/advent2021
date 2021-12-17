from collections import defaultdict, Counter
with open("6.txt", "r") as f:
    fish = Counter(map(int, f.readline().split(",")))
for elapsed in range(256):
    _fish = fish
    fish = defaultdict(int)
    for day, count in _fish.items():
        if day == 0:
            fish[8] += count
        i = day - 1
        if i < 0: i = 6
        fish[i] += count
    if elapsed == 79:
        print(sum(fish.values()))
print(sum(fish.values()))