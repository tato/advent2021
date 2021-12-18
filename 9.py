with open("9.txt", "r") as f:
    data = f.readlines()
    width, height = len(data[0].strip()), len(data)
    heightmap = [int(t) for l in data for t in l.strip()]

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return 10
    return heightmap[y*width + x]

risk = 0
sizes = []
for y in range(height):
    for x in range(width):
        if all(map(lambda t: get(x,y) < t, [get(x+1,y), get(x-1,y), get(x,y+1), get(x,y-1)])):
            risk += get(x,y)+1
            visited = set()
            tovisit = [(x,y)]
            while len(tovisit) > 0:
                (vx, vy) = tovisit.pop(0)
                visited.add((vx, vy))
                for vx2, vy2 in [(vx+1,vy), (vx-1,vy), (vx,vy+1), (vx,vy-1)]:
                    if get(vx2, vy2) > get(vx, vy) and get(vx2, vy2) < 9:
                        tovisit.append((vx2, vy2))
            sizes.append(len(visited))
print(risk)
sizes = sorted(sizes, reverse=True)
print(sizes[0]*sizes[1]*sizes[2])
