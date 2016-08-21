names = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
digit_order = [0,2,4,6,8,5,7,3,9,1]

import re

def is_in(string, substring):
    temp = string
    for c in substring:
        if c in temp:
            temp = remove(temp, c)
        else: return False
    return True

def remove(string, chr):
    i = string.index(chr)
    return string[:i]+string[i+1:]

infile = "/Users/Christopher/Downloads/A-large.in-3.txt"
outfile = "/Users/Christopher/Desktop/Python/CodeJam/1B/output.txt"
txt = open(infile)
data = txt.read()
lines = [l for l in re.split('\n+', data) if l][1:]

newlines = []
for i,l in enumerate(lines):
    line = "Case #" + str(i+1) +": "
    
    numbers = []
    for i in digit_order:
        name = names[i]
        while is_in(l, name):
            numbers.append(i)
            for c in name:
                l = remove(l,c)
    number = sorted(numbers)
    number = ''.join([str(i) for i in number])
    line += number
    newlines.append(line)

lines = '\n'.join(newlines)

target = open(outfile, 'w')
target.write(lines)
