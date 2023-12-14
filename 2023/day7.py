from collections import Counter
from itertools import product

order = "AKQJT98765432"

input_lines = [
"32T3K 765",
"T55J5 684",
"KK677 28",
"KTJJT 220",
"QQQJA 483"
]

#
# read from file
#
with open('input\input_7.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

def score_hand(combo):
    match [b for _, b in Counter(combo).most_common()]:
        case 5, *_:
            return 1
        case 4, *_:
            return 2
        case 3, 2, *_:
            return 3
        case 3, *_:
            return 4
        case 2, 2, *_:
            return 5
        case 2, *_:
            return 6
        case _:
            return 7

res = []
for line in input_lines:
    cards, pts = line.split()
    res.append((score_hand(cards), [order.index(x) for x in cards], int(pts)))

res.sort(reverse = True)
i = 0
total = 0
for score, combo, value in res:
    i = i + 1
    total+=i*value

print(sum((i + 1) * v[-1] for i, v in enumerate(res)))


order = "AKQT98765432J"
res = []

for line in input_lines:
    cards, pts = line.split()
    score = score_hand(cards)
    for subs in product(order[:-1], repeat=cards.count("J")):
        score = min(score, score_hand(cards.replace("J", "") + "".join(subs)))
    res.append((score, [order.index(x) for x in cards], int(pts)))

res.sort(reverse=True)
print(sum((i + 1) * v[-1] for i, v in enumerate(res)))
