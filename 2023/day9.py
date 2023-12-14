from itertools import pairwise

with open('input\input_9.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

'''
input_lines = [
"0 3 6 9 12 15",
"1 3 6 10 15 21",
"10 13 16 21 30 45"
]
'''

def predict(values):
    if all(v == 0 for v in values):
        return 0
    diffs = [b - a for a, b in pairwise(values)]
    return values[-1] + predict(diffs)

res = 0
for line in input_lines:
    values = list(map(int, line.split()))
    res += predict(values)

print("day 9, part 1", res)

res = 0
for line in input_lines:
    values = list(reversed(list(map(int, line.split()))))
    res += predict(values)

print("day 9, part 2", res)    