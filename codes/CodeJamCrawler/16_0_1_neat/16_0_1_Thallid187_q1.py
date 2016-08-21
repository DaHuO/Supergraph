
def digitise(num):
    l = []
    while num > 0:
        l.append(num % 10)
        num = num // 10
    
    return l

def updateDigits(digits, n):
    l = digitise(n)

    for i in l:
        digits[i] = True
    return

def isFinished(digits):
    for i in digits:
        if i == False:
            return False
            
    return True
    

f = open('A-large.in', 'r')
o = open('out.txt', 'w')
T = f.readline()
T = int(T)
for t in range(1, T+1):
    s = f.readline()
    s = s.split()
    s = map(int, s)
    N = s[0]
    
    if N == 0:
        outline = "Case #%d: INSOMNIA\n" % (t)
        o.write(outline)
        continue
    else: 
        finish = False
        digits = [False for x in range(10)]
        inc = 0
        while finish == False:
            inc += 1
            num = N * inc
            updateDigits(digits, num)
            finish = isFinished(digits)                
                     
    outline = "Case #%d: %d\n" % (t, num)
    o.write(outline)

o.close()
