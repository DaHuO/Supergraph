import sets
f = open('test.txt','r')
data = f.readlines()
NUM = data[0]


def detect(N):
    digits = sets.Set()
    for i in xrange(1,1000000):
        digits.update(list(str(i*N)))
        if len(digits)==10:
            return str(i*N)
    return "INSOMNIA"

k = 1
f = open("output.txt",'w')



numbers = map(lambda i: int(i), data[1:])
for N in numbers:
    f.write("Case #%d: %s\n"%(k,detect(N)))
    k+=1
f.close()

f = open("output.txt",'r')
data = f.read()
f.close()
f = open("correct.txt",'r')
correct = f.read()
f.close()
if data==correct:
    print "CORRECT"
else:
    print "FAILED"
