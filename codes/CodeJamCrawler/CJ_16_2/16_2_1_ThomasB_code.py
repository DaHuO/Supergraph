LETTERS = ['Z','E','R','O','N','T','W','H','F','U','V','S','I','X','G']
COUNT_0 = [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
COUNT_1 = [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0]
COUNT_2 = [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0]
COUNT_3 = [0,2,1,0,0,1,0,1,0,0,0,0,0,0,0]
COUNT_4 = [0,0,1,1,0,0,0,0,1,1,0,0,0,0,0]
COUNT_5 = [0,1,0,0,0,0,0,0,1,0,1,0,1,0,0]
COUNT_6 = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]
COUNT_7 = [0,2,0,0,1,0,0,0,0,0,1,1,0,0,0]
COUNT_8 = [0,1,0,0,0,1,0,1,0,0,0,0,1,0,1]
COUNT_9 = [0,1,0,0,2,0,0,0,0,0,0,0,1,0,0]

def read(name):
    return [s.split('\n')[0] for s in open(name,'r').readlines()[1:]]
    
def count(s):
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for c in s:
        counts[LETTERS.index(c)] += 1
    return counts
    
def subtract_counts(c1,c2):
    # subtract c2 from c1
    return [v1-v2 for v1,v2 in zip(c1,c2)]
    
def find_number(counts):
    number = []
    
    for zero in range(0,counts[LETTERS.index('Z')]):
        counts = subtract_counts(counts,COUNT_0)
        number.append(0)
        
    for six in range(0,counts[LETTERS.index('X')]):
        counts = subtract_counts(counts,COUNT_6)
        number.append(6)
        
    for eight in range(0,counts[LETTERS.index('G')]):
        counts = subtract_counts(counts,COUNT_8)
        number.append(8)
        
    for seven in range(0,counts[LETTERS.index('S')]):
        counts = subtract_counts(counts,COUNT_7)
        number.append(7)
        
    for seven in range(0,counts[LETTERS.index('V')]):
        counts = subtract_counts(counts,COUNT_5)
        number.append(5)
        
    for nine in range(0,counts[LETTERS.index('I')]):
        counts = subtract_counts(counts,COUNT_9)
        number.append(9)
        
    for four in range(0,counts[LETTERS.index('U')]):
        counts = subtract_counts(counts,COUNT_4)
        number.append(4)
        
    for three in range(0,counts[LETTERS.index('H')]):
        counts = subtract_counts(counts,COUNT_3)
        number.append(3)
        
    for one in range(0,counts[LETTERS.index('E')]):
        counts = subtract_counts(counts,COUNT_1)
        number.append(1)
        
    for two in range(0,counts[LETTERS.index('O')]):
        counts = subtract_counts(counts,COUNT_2)
        number.append(2)
    
    return sorted(number)
    

cases = read('A-large.in')
numbers = []
for case in cases:
    counts = count(case)
    number = find_number(counts)
    numbers.append(number)

outfile = open('out','w')
for i,number in enumerate(numbers):
    outfile.write('Case #%s: %s\n' % (i+1,''.join([str(n) for n in number])))
outfile.close()
    