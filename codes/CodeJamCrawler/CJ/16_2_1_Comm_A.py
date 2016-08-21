import numpy as np

def output(i, out):
    with open('A-large.out', 'a') as outfile:
        outfile.write("Case #{0}: {1}\n".format(i, out))
letters = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
numbers = range(10)

numtolet = {x:y for (x,y) in zip(numbers, letters)}
lettonum = {x:y for (x,y) in zip(letters, numbers)}


uniquedict1 = {
    "Z": 0,
    "W": 2,
    "H": 3,
    "U": 4,
    "X": 6,
    "G": 8
}

uniquedict2 ={
    "O": 1,
    "F": 5,
    "S": 7
}

def processuniquedict(string, udict):
    numbers = []
    for key in udict.keys():
        charcount = string.count(key)
        numbers.extend(charcount*[udict[key]])
        for char in list(numtolet[udict[key]]):
            string = string.replace(char, '', charcount)
            
    return numbers, string

def solve(i, line): 
    string = str(line).replace('\n','')
    numbers = []
    n1, string = processuniquedict(string, uniquedict1)
    n2, string = processuniquedict(string, uniquedict2)
    numbers.extend(n1)
    numbers.extend(n2)
    nines = string.count('I')
    numbers.extend([9]*nines)
    
    outnum =  ''.join([str(x) for x in sorted(numbers)])
    print outnum
        
    output(i, outnum)
        

lines = open('A-large.in').readlines()

for i, line in enumerate(lines):
    if i > 0:
        solve(i, line)