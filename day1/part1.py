with open("input.txt") as f:
    data = f.read()

lines = data.strip().split("\n")

columns = list(zip(*[map(int, line.split()) for line in lines]))

column1, column2 = sorted(columns[0]), sorted(columns[1])

total = sum([abs(col1 - col2) for col1, col2 in zip(column1, column2)])

print(total)