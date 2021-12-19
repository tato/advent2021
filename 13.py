from collections import namedtuple
Dot = namedtuple("Dot", ["x", "y"])
dots, folds = set(), []
with open("13.txt", "r") as f:
    for l in map(str.strip, f.readlines()):
        if l.startswith("fold along "):
            folds.append(l[11:].split("="))
        elif len(l) > 0:
            [x, y] = l.split(",")
            dots.add(Dot(int(x), int(y)))
for i, [foldaxis, foldpos] in enumerate(folds):
    foldpos = int(foldpos)    
    todel, toadd = set(), set()
    for dot in dots:
        dot = dot._asdict()
        if dot[foldaxis] >= foldpos:
            todel.add(Dot(**dot))
            diff = dot[foldaxis] - foldpos
            dot[foldaxis] = dot[foldaxis] - diff*2
            toadd.add(Dot(**dot))
    dots = dots.union(toadd).difference(todel)
    if i == 0: print(len(dots))

minx, miny, maxx, maxy = 9999, 9999, 0, 0
for dot in dots:
    if dot.x < minx: minx = dot.x
    if dot.x > maxx: maxx = dot.x
    if dot.y < miny: miny = dot.y
    if dot.y > maxy: maxy = dot.y
assert(minx == 0 and miny == 0)
width, height = maxx+1, maxy+1
codemap = ["."]*width*height
for dot in dots:
    codemap[dot.y*width+dot.x] = "#"
for i in range(height):
    print("".join(codemap[i*width:i*width+width]))