with open("7.txt", "r") as f:
    crabs = [int(x) for x in f.readline().split(",")]

def getfuel(center):
    return sum(sum(range(1, abs(c-center)+1)) for c in crabs)

center = round(sum(crabs) / len(crabs))
fuel = getfuel(center)

if getfuel(center-1) <= fuel:
    move = -1
elif getfuel(center+1) <= fuel:
    move = +1
else:
    print(fuel)
    exit(0)

while fuel >= getfuel(center):
    fuel = getfuel(center)
    center += move
print(fuel)