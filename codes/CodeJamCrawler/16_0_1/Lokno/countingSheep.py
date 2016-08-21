# Author      : Jonathan Decker
# Description : Problem A. Counting Sheep

# gets an array of digits from an integer x
def getDigits( x ):
    d = []
    while x > 0:
        d.append(x % 10)
        x /= 10
    return d

# sets bits for each present digit in integer x
def mapBits( b, x ):
    for d in getDigits(x):
        b |= (1 << d)
    return b

# returns last number before all digits 0-9 are
# found in the sequence n*i where i == 
def CountingSheep( n ):
    b = 0
    i = 1
    x = 0
    ret = "INSOMNIA"
    
    if n != 0:
        while b != 1023:
            x = n*i
            b = mapBits(b,x) 
            i += 1

        if b == 1023:
            ret = x

    return ret

numLines = input()
for i in range(numLines):
    val = input()
    print("Case #%d: %s" % ( i+1, CountingSheep( val ) ))