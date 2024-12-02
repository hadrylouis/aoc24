with open("input.txt") as f:
    data = f.read()

lines = data.strip().split("\n")

columns = list(zip(*[map(int, line.split()) for line in lines]))

occurrences = {num: columns[1].count(num) for num in columns[1]}

score = sum(occurrences.get(num, 0) * num for num in columns[0])

print(score)
