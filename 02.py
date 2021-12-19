
x, y = 0, 0
with open("2.txt", "r") as f:
    for [command, arg] in [ c.split() for c in f.readlines() ]:
        if command == "forward":
            x += int(arg)
        elif command == "up":
            y -= int(arg)
        elif command == "down":
            y += int(arg)
    print(x * y)