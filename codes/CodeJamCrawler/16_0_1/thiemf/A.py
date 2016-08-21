import sys

f = open(sys.argv[1], 'r')
t = int(f.readline())
for i in range(1, t+1):
    n = int(f.readline())
    
    if n == 0:
        print "Case #" + str(i) + ": INSOMNIA"
        continue    
    
    j = 1
    digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    while len(digits) > 0:
        nmult = n*j
        for c in str(nmult):
            if c in digits:
                digits.remove(c)
        j=j+1
    
    print "Case #" + str(i) + ": " + str(nmult)
        
    
