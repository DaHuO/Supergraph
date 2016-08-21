fo = open("B-large.in", "r")
counter = 0;
b = [];
anotherCounter = 0;
pick='';
plus = '+';
minus = '-';
times = 0;
master=1;
answers = [];
def flip(s):
    time = 0
    while('-' in s):
        start = s[0]
        if start == '-':
            end = '+'
        else:
            end = '-'
        index = s.find(end)
        if index < 0:
            index = len(s)
        s = s.replace(start, end, index)
        time += 1
    return time

for line in fo:
    counter +=1
    if counter ==1:
        total = line;
        #print ('THis total',total);
    else:
        line = line.strip();
        line = str(line);
        result = flip(line);
        print('Flip line',result);
        answers.append(result);
with open('pancakes.txt', 'w') as f:
    case_number = 1
    for n in answers:
        f.write('Case #{0}: {1}\n'.format(case_number, n))
        case_number += 1