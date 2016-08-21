"""
test = "123456789"
pos = test.rfind('9')
print test[:pos+1]
print test[pos+1:]
"""

def flipPancake(cakes):
    newcakes = ''
    for cake in cakes:
        if ( cake == '-' ):
            newcakes += '+'
        else:
            newcakes += '-'

    return newcakes

def makeHappy(cakes, trycount):
    if ( len(cakes) >= 1 and len(cakes) <= 100 ):
        #make logic
        pos = cakes.rfind('-')
        if ( pos == -1 ):
            return trycount
        else:
            cakes = flipPancake(cakes[:pos+1]) + cakes[pos+1:]
            #print cakes
            return makeHappy(cakes, trycount+1)
    else:
        return -1 #error code

"""
cakes = "--+-"
print str(makeHappy( cakes, 0 ))
"""

f = open ( "./B-large.in", 'r' )
foutput = open ( "./output_large.txt", 'w')
T = int(f.readline())
if T >= 1 and T <= 100:
    i = 1
    while True:
        input = f.readline()
        if not input:
            break

        pancake = input.replace('\n','')
        trycount = 0
        answer = str(makeHappy(pancake, 0))
        output = 'Case #'+ str(i) + ': ' + answer + '\n'
        foutput.write(output)
        i = i+1
else:
    print('Limits Invalid')

f.close()
foutput.close()
