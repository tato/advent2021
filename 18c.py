
def add(a, b):
    su = f"[{a},{b}]"
    return reduce(su)

def reduce(number):
    done = False
    while not done:
        previous = ""
        while previous != number:
            previous = number
            number = explode(number)
        number = split(number)
        done = previous == number
    return number

def explode(number):
    nesting = 0
    exploding_pair_start = 0
    for i, n in enumerate(number):
        if n == "[":
            nesting += 1
            if nesting < 5: continue
            exploding_pair_start = i
            break
        if n == "]":
            nesting -= 1
    if exploding_pair_start == 0:
        return number
    
    exploding_pair_stop = number.find("]", exploding_pair_start)
    pair = number[exploding_pair_start+1:exploding_pair_stop]
    regular_numbers = [ int(x) for x in pair.split(",") ]

    left_part = number[:exploding_pair_start]
    for i in range(len(left_part)-1, -1, -1):
        if not left_part[i].isdigit():
            continue
        if left_part[i-1].isdigit():
            print("left part 2")
            x = int(left_part[i-1:i+1])
            left_part = f"{left_part[:i-1]}{x + regular_numbers[0]}{left_part[i+1:]}"
            break
        y = int(left_part[i])
        left_part = f"{left_part[:i]}{y + regular_numbers[0]}{left_part[i+1:]}"
        break

    right_part = number[exploding_pair_stop+1:]
    for i in range(len(right_part)):
        if not right_part[i].isdigit():
            break
        if right_part[i+1].isdigit():
            print("right part 2")
            x = int(right_part[i:i+2])
            right_part = f"{right_part[:i]}{x + regular_numbers[1]}{right_part[i+2:]}"
            break
        y = int(right_part[i])
        right_part = f"{right_part[:i]}{y + regular_numbers[1]}{right_part[i+1:]}"
        break

    return f"{left_part}0{right_part}"

def split(number):
    for i in range(len(number)):
        if not number[i].isdigit(): continue
        if not number[i+1].isdigit(): continue

        x = int(number[i:i+2])
        number = f"{number[:i]}[{x//2},{x//2+x%2}]{number[i+2:]}"
        break
    return number

class TreeNode:
    def __init__(self, tokens):
        token = tokens.pop()
        if token.isdigit():
            self.left = None
            self.right = None
            self.is_leaf = True
            self.number = int(token)
        else:
            if token != "]": raise Exception
            self.right = TreeNode(tokens)
            tokens.pop()
            self.left = TreeNode(tokens)
            tokens.pop()
            self.is_leaf = False

    def parse(number):
        return TreeNode(list(number))
    
    def magnitude(self):
        if self.is_leaf:
            return self.number
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

def magnitude(number):
    tree = TreeNode.parse(number)
    return tree.magnitude()

with open("18.txt", "r") as f:
    numbers = [ l.strip() for l in f.readlines() ]
su = numbers[0]
for n in numbers:
    su = add(su, n)
print(magnitude(su))