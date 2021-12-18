from collections import defaultdict
with open("12.txt", "r") as f:
    caves = defaultdict(set)
    for l in f.readlines():
        [a, b] = l.strip().split("-")
        caves[a].add(b)
        caves[b].add(a)
isnotend = lambda path: "end" not in path
paths = {("start",)}
while any(map(isnotend, paths)):
    for path in [p for p in paths if isnotend(p)]:
        for nxtroom in caves[path[-1]]:
            if nxtroom.islower() and nxtroom in path:
                continue
            if (*path, nxtroom) not in paths:
                paths.add((*path, nxtroom))
        paths.remove(path)
print(len(paths))