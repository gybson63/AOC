import sys

#
# remove all none-digit from string
#
def delete_letters(s : str)->str:
    res = ""
    for ch in s:
        if ch.isdigit():
            res+=ch
    
    return res

#
# score lines
#
def score_lines(lines)->int:
    result = 0
    for line in lines:
        if len(line)==1:
            num = line[0]+line[0]
        else:
            num = line[0]+line[-1]
        result += int(num)
    return result

#
# read from file
#
with open('input\input_1.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

#
# prepare lines
#
lines = []
for line in input_lines:
    lines.append(delete_letters(line))

print("day 1, part 1:", score_lines(lines))

digi_dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

#
# check if string is digit
#
def literal_digit(s:str)->str:
    for key,value in digi_dic.items():
        if s[0:len(key)] == key:
            return str(value)
    return ""

#
# remove letters and add spelled digits 
#
def delete_letters2(s : str)->str:
    res = ""
    for i in range(len(s)):
        ch = s[i]
        if ch.isdigit():
            res+=ch
        else:
            lit = literal_digit(s[i:])
            if lit!="":
                res+=lit
    
    return res

#
# prepare lines
#
lines = []
for line in input_lines:
    lines.append(delete_letters2(line))

print("day 1, part 2:", score_lines(lines))