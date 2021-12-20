from collections import deque
import sys
with open("15.txt", "r") as f:
    data = f.readlines()
    width, height = len(data[0].strip()), len(data)
    riskmap = [int(x) for l in data for x in l.strip()]

processedrisk = [sys.maxsize] * len(riskmap)
toprocess = { (0,0,0) }
processed = set()
while toprocess:
    posx, posy, risk = sorted(toprocess, key=lambda p: p[2])[0]
    toprocess.remove((posx, posy, risk))
    processed.add((posx, posy))
    if posx == width-1 and posy == height-1:
        print(risk)
        break
    for movex, movey in ((-1,0), (1,0), (0,-1), (0,1)):
        nextx, nexty = posx+movex, posy+movey
        if nextx < 0 or nexty < 0 or nextx >= width or nexty >= height:
            continue
        if (nextx, nexty) in processed:
            continue
        nextrisk = risk + riskmap[nexty*width+nextx]
        if nextrisk < processedrisk[nexty*width+nextx]:
            processedrisk[nexty*width+nextx] = nextrisk
            toprocess.add((nextx, nexty, nextrisk))

