from collections import Counter

def getmaxi(i,counts):
    cm=1000
    if i == 0:
        cm = min(counts['Z'], cm)
        cm = min(counts['E'], cm)
        cm = min(counts['R'], cm)
        cm = min(counts['O'], cm)
    elif i == 1:
        cm = min(counts['E'], cm)
        cm = min(counts['N'], cm)
        cm = min(counts['O'], cm)
    elif i == 2:
        cm = min(counts['T'], cm)
        cm = min(counts['W'], cm)
        cm = min(counts['O'], cm)
    elif i == 3:
        cm = min(counts['T'], cm)
        cm = min(counts['H'], cm)
        cm = min(counts['R'], cm)
        cm = min(counts['E'] / 2, cm)
    elif i == 4:
        cm = min(counts['F'], cm)
        cm = min(counts['O'], cm)
        cm = min(counts['U'], cm)
        cm = min(counts['R'], cm)
    elif i == 5:
        cm = min(counts['F'], cm)
        cm = min(counts['I'], cm)
        cm = min(counts['V'], cm)
        cm = min(counts['E'], cm)
    elif i == 6:
        cm = min(counts['S'], cm)
        cm = min(counts['I'], cm)
        cm = min(counts['X'], cm)
    elif i == 7:
        cm = min(counts['S'], cm)
        cm = min(counts['E'] / 2, cm)
        cm = min(counts['V'], cm)
        cm = min(counts['N'], cm)
    elif i == 8:
        cm = min(counts['E'], cm)
        cm = min(counts['I'], cm)
        cm = min(counts['G'], cm)
        cm = min(counts['T'], cm)
        cm = min(counts['H'], cm)
    elif i == 9:
        cm = min(counts['N'], cm)
        cm = min(counts['I'], cm)
        cm = min(counts['N'], cm)
        cm = min(counts['E'], cm)
    return cm


def subtract(times,i,counts):
    if i==0:
        counts['Z'] -= 1 * times
        counts['E'] -= 1 * times
        counts['R'] -= 1 * times
        counts['O'] -= 1 * times
    elif i==1:
        counts['E'] -= 1 * times
        counts['N'] -= 1 * times
        counts['O'] -= 1 * times
    elif i == 2:
        counts['T'] -= 1 * times
        counts['W'] -= 1 * times
        counts['O'] -= 1 * times
    elif i == 3:
        counts['T'] -= times
        counts['H'] -= times
        counts['R'] -= times
        counts['E'] -= times
        counts['E'] -= times
    elif i == 4:
        counts['F'] -= times
        counts['O'] -= times
        counts['U'] -= times
        counts['R'] -= times
    elif i == 5:
        counts['F'] -= times
        counts['I'] -= times
        counts['V'] -= times
        counts['E'] -= times
    elif i == 6:
        counts['S'] -= times
        counts['I'] -= times
        counts['X'] -= times
    elif i == 7:
        counts['S'] -= times
        counts['E'] -= times
        counts['V'] -= times
        counts['E'] -= times
        counts['N'] -= times
    elif i == 8:
        counts['E'] -= times
        counts['I'] -= times
        counts['G'] -= times
        counts['T'] -= times
        counts['H'] -= times
    elif i == 9:
        counts['N'] -= times
        counts['I'] -= times
        counts['N'] -= times
        counts['E'] -= times

def emptys(remCounts):
    return all([x==0 for x in remCounts.values()])

def rec(remCounts,digit,cursol):
    #print "Cursol: " + cursol + ", remCounts: " + str(remCounts)
    if emptys(remCounts):
        return cursol
    if digit > 9:
        return None
    maxi=getmaxi(digit,remCounts)
    for i in reversed(range(maxi+1)):
        cp=remCounts.copy()
        #print cp
        print "Testing digit " + str(digit) + ", " + str(i) + " times."
        subtract(i, digit, cp)
        cpsol = cursol + ''.join(str(digit) for j in range(i))
        nsol = rec(cp,digit+1,cpsol)
        if not nsol is None:
            return nsol
    return None



def getans(el):
    counts=Counter(el)
    del counts['\n']
    #print counts
    return rec(counts,0,"")
	
def glfs(s):
	return s.split(' ')

def gilfs(s):
	return [int(x) for x in glfs(s)]

fileName = "A-small-attempt1.in"
f = open(fileName)

l=f.readline()
l=f.readline()

inputs=[]
while l:
    inputs.append(l)
    l=f.readline()
    
f.close()

outfile="tst1.out"
of=open(outfile,"wb")
testCount=1

for inputEl in inputs:
    ans = getans(inputEl)
    of.write("Case #" + str(testCount) + ": " + str(ans)+'\n')
    testCount += 1

of.close()

