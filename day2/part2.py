def is_safe(line):
    diffs = [line[i+1] - line[i] for i in range(len(line) - 1)]
    is_increasing = all(diff > 0 for diff in diffs)
    is_decreasing = all(diff < 0 for diff in diffs)
    is_within_range = all(1 <= abs(diff) <= 3 for diff in diffs)

    return (is_increasing or is_decreasing) and is_within_range

def is_safe_with_dampener(line):
    if is_safe(line):
        return True
    
    for i in range(len(line)):
        modified_line = line[:i] + line[i+1:]
        if is_safe(modified_line):
            return True
    
    return False

with open("input.txt") as f:
    data = f.read()

lines = [list(map(int, line.split())) for line in data.strip().split("\n")]

safe = 0
for line in lines:
    if is_safe_with_dampener(line):
        safe += 1

print(safe)