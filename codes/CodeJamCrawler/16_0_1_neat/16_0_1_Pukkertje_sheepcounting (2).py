f = open('A-large.in', 'r')
o = open('output', 'w')
# Total amount of test cases
t = int(f.readline())

for x in range(1, t + 1):
    # Which have occurred
    b = 0b0
    #n = int(input())
    n = int(f.readline())
    c = 1
    
    if(n == 0):
        o.write("Case #%s: INSOMNIA\n" % (x))
        continue
    
    while b != 0b1111111111:
        for num in str(n * c):
            b |= 1 << int(num)
            
        c = c + 1
    
    o.write("Case #%s: %d\n" % (x, n * (c - 1)))

o.close()
f.close()