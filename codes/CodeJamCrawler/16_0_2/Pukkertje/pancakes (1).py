f = open('B-large.in', 'r')
o = open('output', 'w')
# Total amount of test cases
t = int(f.readline())

for x in range(1, t + 1):
    # Get stack without nl
    s = list(f.readline().rstrip('\n'))
    c = 1
    
    if(s.count('-') == 0):
        o.write("Case #%s: 0\n" % (x))
        continue
    
    if(s.count('-') == 1 and len(s) == 1):
        o.write("Case #%s: 1\n" % (x))
        continue
    
    while s.count('-') != 0:
        i = len(s) - 1 - s[::-1].index('-')
        s[:i+1] = ['-' if x=='0' else x for x in ['+' if x=='-' else x for x in ['0' if x=='+' else x for x in s[:i+1]]]]
        c = c + 1
    
    o.write("Case #%s: %d\n" % (x, (c - 1)))

o.close()
f.close()