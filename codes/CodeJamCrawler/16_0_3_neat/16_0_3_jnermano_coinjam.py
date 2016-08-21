import math

def primerOrNot(num):
    if num % 2 == 0:
        return 2
    
    r = math.floor(math.sqrt(num))
    k = 3
    while k <= r:
        if num % k == 0:
            return k
        k += 2
    return 0


t = input()
inp = [int(x) for x in raw_input().split(' ')]
N = inp[0]
J = inp[1]
coinjams = dict()

start_num = '1'+('0'*(N-2))+'1'
while len(coinjams) < J: #10 and len(start_num) == N:
    bases = []
    for i in range(2, 11):
        b = int(start_num, i)
        ret = primerOrNot(b)
        if ret > 0:
            bases.append(ret)
    if len(bases) == 9:
        coinjams[start_num] = bases
    
    tmp = long(start_num, 2) + 2
    start_num = bin(tmp)[2:]

print "Case #{}:".format(t)
for key, value in coinjams.items():
    print "{} {} {} {} {} {} {} {} {} {}".format(key, value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8])


