import math

times = [41, 66, 72, 66]
distances = [244, 1047, 1228, 1040]

#times = [7, 15, 30]
#distances = [9, 40, 200]

res = 1
for time, distance in zip(times, distances):
    vars = 0
    for i in range(time):
        if i*(time-i)>distance:
            vars += 1
    res *= vars

print("day 6, part 1", res)

#time = 71530
#distance = 940200
time = 41667266
distance = 244104712281040

# S = T * (T-v)
# v^2-Tv+S = 0
# D = T^2 - 4*S
# x1 = (T + sqrt(T^2 - 4*S))/2; x2 = (T - sqrt(T^2 - 4*S))/2

x1 = math.floor(time + math.sqrt(time**2 - 4*distance)/2)
x2 = math.ceil(time - math.sqrt(time**2 - 4*distance)/2)

print("day 6, part 1", x1-x2+1)
