with open("input.txt") as f:
    data = f.read()

lines = [list(map(int, line.split())) for line in data.strip().split("\n")]

safe = 0
for line in lines:
    diffs = diffs = [line[i+1] - line[i] for i in range(len(line) - 1)]
    if all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs):
        if all(abs(diff) <= 3 for diff in diffs):
            safe += 1

print(safe)