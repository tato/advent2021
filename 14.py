from collections import Counter, defaultdict

with open("14.txt", "r") as f:
    polymer = f.readline().strip()
    f.readline()
    rules = { i.strip(): o.strip() for [i, o] in (line.split("->") for line in f.readlines()) }

first, last = polymer[0], polymer[-1]
pairs = [polymer[i]+polymer[i+1] for i in range(len(polymer)-1)]
pairs = Counter(pairs)

for step in range(40):
    nextstep = defaultdict(int)
    for pair, count in pairs.items():
        if pair in rules:
            nextstep[pair[0]+rules[pair]] += count
            nextstep[rules[pair]+pair[1]] += count
    pairs = nextstep
    if step == 9 or step == 39:
        counts = defaultdict(int)
        counts[first] += 1
        counts[last] += 1
        for pair, count in pairs.items():
            counts[pair[0]] += count
            counts[pair[1]] += count
        print((max(counts.values())-min(counts.values()))//2)