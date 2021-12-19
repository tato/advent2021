with open("8.txt", "r") as f:
    entries = [[[set(x) for x in sec.strip().split()] for sec in l.split("|")] for l in f.readlines()]

def decode(digits, display):
    one = next(filter(lambda x: len(x) == 2, digits))
    four = next(filter(lambda x: len(x) == 4, digits))
    seven = next(filter(lambda x: len(x) == 3, digits))
    eight = next(filter(lambda x: len(x) == 7, digits))
    for seg in one:
        deduc = list(filter(lambda x: seg not in x, digits))
        if len(deduc) == 1:
            two = deduc[0]
        else:
            [five, six] = deduc
            if len(five) != 5:
                five, six = six, five
    nine = eight.difference(six.difference(five))
    three = nine.difference(eight.difference(one.union(two)))
    for d in digits:
        if d not in [one, two, three, four, five, six, seven, eight, nine]:
            zero = d
            break

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]

    decoded = 0
    for i, d in enumerate(display):
        decoded += digits.index(d) * 10**(4-i-1)
    return decoded

print(sum(1 for [_, display] in entries for d in display if len(d) in [2,3,4,7]))
print(sum(decode(digits, display) for [digits, display] in entries))