#CNT=50
#WIDTH=6
CNT=500
WIDTH=14
print "Case #1:"
for i in range(CNT):
    s = bin(i)[2:]
    s = s.rjust(WIDTH,'0')
    s = '1'+s+'1'
    ss = s+s
    d = map(str,[int(s,base) for base in range(2,11)])
    print " ".join([ss]+d)

