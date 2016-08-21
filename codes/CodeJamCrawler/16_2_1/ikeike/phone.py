import sys

stream = sys.stdin


t = int(stream.readline().strip())

for pp in range(t):
    s = stream.readline().strip()
    digits = [0]*10
    digits[6] = s.count('X')
    digits[7] = s.count('S') - digits[6]
    digits[0] = s.count('Z')
    digits[5] = s.count('V') - digits[7]
    digits[8] = s.count('G')
    digits[4] = s.count('U')
    digits[2] = s.count('W')
    digits[3] = s.count('T') - digits[8] - digits[2]
    digits[1] = s.count('O') - digits[0] - digits[2] - digits[4]
    digits[9] = (s.count('N')-digits[7] - digits[1])/2
    #print digits
    dd = []
    for i,di in enumerate(digits):
        dd += di*[i]
    #dd = [k for k,dk in enumerate(digits) if dk!=0]
    dd.sort()
    dd = [str(k) for k in dd]
    print "Case #"+str(pp+1)+":", "".join(dd)
