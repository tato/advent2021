with open("3.txt", "r") as f:
    numbers = [x.strip() for x in f.readlines()]

def getcommon(xs, i):
    s = sum([int(n[i]) for n in xs])
    return int(s >= len(xs) - s)


common = [getcommon(numbers, i) for i in range(len(numbers[0]))]
gamma = int("".join([str(x) for x in common]), 2)
epsilon = int("".join([str(1-x) for x in common]), 2)
print(gamma*epsilon)


oxygen = list(numbers)
co2 = list(numbers)
for i in range(len(numbers[0])):
    if len(oxygen) != 1:
        common = getcommon(oxygen, i)
        oxygen = [ n for n in oxygen if int(n[i]) == common ]
    if len(co2) != 1:
        common = getcommon(co2, i)
        co2 = [ n for n in co2 if int(n[i]) != common ]

print(int(oxygen[0], 2) * int(co2[0], 2))