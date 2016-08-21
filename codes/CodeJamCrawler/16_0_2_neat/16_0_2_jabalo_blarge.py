f = open('/Users/jacquelineabalo/Documents/B-large.in');
lines = f.readlines();
target = open('/Users/jacquelineabalo/Documents/blargeresult.txt', 'w');

for i in range(1, len(lines)):
    flips = 0;
    pancakes = lines[i].strip();
    if pancakes[0]=='+':
        sign = 1;
    else:
        sign = 0;
    j = 0;
    while j!=(len(pancakes)-1):
        if pancakes[j]!=pancakes[j+1]:
            flips = flips + 1;
            sign = 1 - sign;
        j = j + 1;
    if sign==0:
        flips = flips + 1;
    target.write('Case #' + str(i) + ': ' + str(flips) + '\n');
target.close();
f.close();
print('done');
           
        
    
