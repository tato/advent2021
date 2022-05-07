import math, dataclasses

logger = open("log.txt", "w")

with open("18.txt", "r") as f:
    numbers = [eval(n) for n in f.readlines()]

def reduce(_number, exit_after_one=False):
    print(f"reducing {_number}", file=logger)

    @dataclasses.dataclass
    class Cell: n: int

    def create_cells(number):
        if isinstance(number, int): return Cell(number)
        else: return [ create_cells(number[0]), create_cells(number[1]) ]
    def remove_cells(number):
        if isinstance(number, Cell): return number.n
        else: return [ remove_cells(number[0]), remove_cells(number[1]) ]

    _number = create_cells(_number)

    @dataclasses.dataclass
    class ReduceContext:
        add_to_next: int = None
        last_cell_found: Cell = None
        changed: bool = False

        def _reduce(self, number, nesting=1):
            if not self.changed and isinstance(number, list) and isinstance(number[0], Cell) and nesting > 4:
                print(f"  explode pair [{number[0].n}, {number[1].n}]", file=logger)
                if self.last_cell_found != None:
                    self.last_cell_found.n += number[0].n
                self.add_to_next = number[1].n
                self.changed = True
                return Cell(0)
            elif not self.changed and isinstance(number, Cell) and number.n > 9:
                print(f"  split number {number.n}", file=logger)
                self.changed = True
                return [Cell(math.floor(number.n / 2)), Cell(math.ceil(number.n / 2))]
            elif isinstance(number, Cell):
                self.last_cell_found = number
                if self.add_to_next != None:
                    number.n += self.add_to_next
                    self.add_to_next = None
                return number
            else:
                left = self._reduce(number[0], nesting+1)
                right = self._reduce(number[1], nesting+1)
                return [ left, right ]
    
    i = 0
    while True:
        ctx = ReduceContext()
        _number = ctx._reduce(_number)
        if not ctx.changed or exit_after_one:
            print(f"done", file=logger)
            break
        else:
            i += 1
            print(f"after {i} iter: {remove_cells(_number)}", file=logger)

    

    return remove_cells(_number)

def magnitude(number):
    if isinstance(number, int):
        return number
    else:
        return 3*magnitude(number[0]) + 2*magnitude(number[1])

def _sum(numbers):
    su = numbers[0]
    for n in numbers[1:]:
        su = reduce([su, n])
    return su

# assert reduce([[[[[9,8],1],2],3],4], True) == [[[[0,9],2],3],4]
# assert reduce([7,[6,[5,[4,[3,2]]]]], True) == [7,[6,[5,[7,0]]]]
# assert reduce([[6,[5,[4,[3,2]]]],1], True) == [[6,[5,[7,0]]],3]
# assert reduce([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], True) == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
# assert reduce([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], True) == [[3,[2,[8,0]]],[9,[5,[7,0]]]]
# assert reduce([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
# assert _sum([[i,i] for i in range(1,5)]) == [[[[1,1],[2,2]],[3,3]],[4,4]]
# assert _sum([[i,i] for i in range(1,6)]) == [[[[3,0],[5,3]],[4,4]],[5,5]]
# assert _sum([[i,i] for i in range(1,7)]) == [[[[5,0],[7,4]],[5,5]],[6,6]]
_sum([[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],[7,[5,[[3,8],[1,4]]]],[[2,[2,2]],[8,[8,1]]],[2,9],[1,[[[9,3],9],[[9,0],[0,7]]]],[[[5,[7,4]],7],1],[[[[4,2],2],6],[8,7]]]) == [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
logger.close()
# print(magnitude(_sum(numbers)))

