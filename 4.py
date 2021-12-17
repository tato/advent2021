from types import SimpleNamespace

with open("4.txt", "r") as f:
    numbers = [ int(x) for x in f.readline().split(",") ]
    boards = []
    while f.readline():
        data = [ int(x) for _ in range(5) for x in f.readline().strip().split() ]
        boards.append(SimpleNamespace(won=False, data=data, found=[False]*25))

wins = 0
for number in numbers:
    for board in boards:
        for i, d in enumerate(board.data):
            if d == number:
                board.found[i] = True

        if not board.won:
            for i in range(5):
                if all(board.found[i*5:i*5+5]) or all(board.found[i:25:5]):
                    wins += 1
                    board.won = True
                    if wins == 1 or wins == len(boards):
                        unmarked = sum(d for d, f in zip(board.data, board.found) if not f)
                        print(unmarked * number)
                    break
