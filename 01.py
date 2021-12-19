with open("1.txt", "r") as f:
    numbers = [ int(x) for x in f.readlines() ]
print(sum([ numbers[i+1] > numbers[i] for i in range(len(numbers)-1)]))
print(sum([ numbers[i+3] > numbers[i] for i in range(len(numbers)-3)]))

