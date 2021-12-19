x, y, aim = 0, 0, 0
with open("2.txt", "r") as f:
    for [command, arg] in [ c.split() for c in f.readlines() ]:
        if command == "forward":
            x += int(arg)
            y += aim * int(arg)
        elif command == "up":
            aim -= int(arg)
        elif command == "down":
            aim += int(arg)
    print(x * y)