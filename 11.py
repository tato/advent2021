with open("11.txt", "r") as f:
    data = f.readlines()
    width, height = len(data[0].strip()), len(data)
    energies = [int(t) for l in data for t in l.strip()]

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return 0
    return energies[y*width + x]
def inc(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return
    energies[y*width + x] += 1
def reset(x, y):
    energies[y*width + x] = 0

count = 0
for i in range(10000):
    energies = [e+1 for e in energies]
    toflash = []
    for y in range(height):
        for x in range(width):
            if get(x, y) > 9:
                toflash.append((x, y))
    flashed = set()
    while len(toflash) > 0:
        x, y = toflash.pop()
        if (x, y) in flashed:
            continue
        flashed.add((x, y))
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0: continue
                inc(x+dx, y+dy)
                if get(x+dx, y+dy) > 9 and (x+dx, y+dy) not in flashed:
                    toflash.append((x+dx, y+dy))
    count += len(flashed)
    for x, y in flashed:
        reset(x, y)

    if i == 99:
        print(f"100 -> {count}")
    if len(flashed) == len(energies):
        print(i+1)
        break

