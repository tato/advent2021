import math
with open("19.txt", "r") as f:
    scanners = []
    for line in map(str.strip, f.readlines()):
        if len(line) == 0:
            scanners.append(scanner)
        elif line.startswith("---"):
            scanner = []
        else:
            scanner.append(eval(line))

def distance(a, b):
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)

# try to match scanners 0 and 1
# find pairs of points from s0, compare them with pairs from s1
for a1, a2 in ((scanners[0][i], scanners[0][i+1]) for i in range(len(scanners[0])-1)):
    for b1, b2 in ((scanners[1][i], scanners[1][i+1]) for i in range(len(scanners[1]-1))):
        # if they're the same distance in both scanners, they might be the same points
        if distance(a1, a2) == distance(b1, b2):
            # what transformation do we have to apply to s1 points so they look the same as s0 points?
            # well... probably impossible to know... because we dont know the orientation.
            # there are two options, either b1 is a1 or b1 is a2.. but then if we have
            #   to figure out where s1 is so that b1 looks like a1... there might be many possibilities
            #    but maybe we dont need to know where s1 is exactly???
            # we might be able to do that with a triangle from each scanner
            pass

# 1304, 1246