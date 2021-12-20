from collections import deque
import sys

def getminrisk(get, width, height):
    processedrisk = [sys.maxsize] * width*height
    toprocess = { (0,0,0) }
    processed = set()
    while toprocess:
        posx, posy, risk = sorted(toprocess, key=lambda p: p[2])[0]
        toprocess.remove((posx, posy, risk))
        processed.add((posx, posy))
        if posx == width-1 and posy == height-1:
            return risk
        for movex, movey in ((-1,0), (1,0), (0,-1), (0,1)):
            nextx, nexty = posx+movex, posy+movey
            if nextx < 0 or nexty < 0 or nextx >= width or nexty >= height:
                continue
            if (nextx, nexty) in processed:
                continue
            nextrisk = risk + get(nextx, nexty)
            if nextrisk < processedrisk[nexty*width+nextx]:
                processedrisk[nexty*width+nextx] = nextrisk
                toprocess.add((nextx, nexty, nextrisk))

with open("15.txt", "r") as f:
    data = f.readlines()
    width, height = len(data[0].strip()), len(data)
    riskmap = [int(x) for l in data for x in l.strip()]

def get(x, y):
    return riskmap[y*width+x]
def get5(x, y):
    xi, yi = x // width, y // width
    truex, truey = x % width, y % height
    return (riskmap[truey*width+truex]+xi+yi-1)%9+1

print(getminrisk(get, width, height))
print(getminrisk(get5, width*5, height*5))
