with open("10.txt", "r") as f:
    nav = [l.strip() for l in f.readlines()]
corrupt = 0
incomplete = []
def corrupt(chunk):
    hist = []
    for c in chunk:
        if c in "([{<":
            hist.append(c)
        elif c == ")":
            if hist.pop() != "(":
                return 3
        elif c == "]":
            if hist.pop() != "[":
                return 57
        elif c == "}":
            if hist.pop() != "{":
                return 1197
        elif c == ">":
            if hist.pop() != "<":
                return 25137
    return 0
def incomplete(chunk):
    if corrupt(chunk) > 0:
        return 0
    hist = []
    for c in chunk:
        if c in "([{<":
            hist.append(c)
        else:
            hist.pop()
    score = 0
    scores = {"(":1, "[":2, "{":3, "<":4}
    for c in hist[::-1]:
        score = score * 5 + scores[c]
    return score
print(sum(map(corrupt, nav)))
completion = [ x for x in map(incomplete, nav) if x > 0]
print(sorted(completion)[len(completion)//2])