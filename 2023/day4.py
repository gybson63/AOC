from collections import defaultdict

#
# read from file
#
with open('input\input_4.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

res = 0
for line in input_lines:
    strip = line[10:].split("|")
    numbers1 = strip[0].split()
    numbers2 = strip[1].split()
    wins = 0
    for num in numbers2:
        if num in numbers1:
            wins+=1
    if wins>0:
        res += 2**(wins-1)

print("day 4, part 1", res)


cards = defaultdict(int)
res = 0
for i in range(len(input_lines)):
    cards[i]+=1
    res +=1
    line = input_lines[i]
    strip = line[10:].split("|")
    numbers1 = strip[0].split()
    numbers2 = strip[1].split()
    wins = 0
    for num in numbers2:
        if num in numbers1:
            wins+=1
            cards[i+wins]+=cards[i]
            res += cards[i]
      
print("day 4, part 2", res)