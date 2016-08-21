from collections import Counter

f = open('A-large.in', 'r')
o = open('out.txt', 'w')
T = f.readline()
T = int(T)
for t in range(1, T+1):
    s = f.readline()
    s = s[:-1]
    
    counter = Counter(s)
    
    counts = [0 for x in range(10)]    
    
    counts[0] = counter['Z']
    for i in range(counts[0]):
        for char in "ZERO":
            counter[char] -= 1

    counts[2] = counter['W']
    for i in range(counts[2]):
        for char in "TWO":
            counter[char] -= 1

    counts[4] = counter['U']
    for i in range(counts[4]):
        for char in "FOUR":
            counter[char] -= 1

    counts[6] = counter['X']
    for i in range(counts[6]):
        for char in "SIX":
            counter[char] -= 1

    counts[8] = counter['G']
    for i in range(counts[8]):
        for char in "EIGHT":
            counter[char] -= 1

    counts[5] = counter['F']
    for i in range(counts[5]):
        for char in "FIVE":
            counter[char] -= 1

    counts[7] = counter['V']
    for i in range(counts[7]):
        for char in "SEVEN":
            counter[char] -= 1
    
    counts[3] = counter['R']
    for i in range(counts[3]):
        for char in "THREE":
            counter[char] -= 1    

    counts[1] = counter['O']
    for i in range(counts[1]):
        for char in "ONE":
            counter[char] -= 1
            
    counts[9] = counter['I']
    for i in range(counts[9]):
        for char in "NINE":
            counter[char] -= 1
    

    ans = ""
    
    for i in range(10):
        for j in range(counts[i]):
            ans += str(i)

    print counter                     
                     
    outline = "Case #%d: " % (t) + ans + "\n" 
    o.write(outline)

o.close()
