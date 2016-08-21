import math

tests = int(input())

for t in xrange(1, tests+1):
    
    n, j = map(int, raw_input().split(' '))
    print "Case #{}:".format(t)

    i = 0
    jamcoins = 0
    while True:
        jam = "1" + ("{0:0" + str(n - 2) + "b}").format(i) + "1"
        
        if len(jam) > n:
            break

        proof = []
        #print "--- {}".format(jam)
        for b in range(2,11):
            num = int(jam, b)
            #print "{} in base {}".format(num, b)
            for a in range(2,int(math.sqrt(num)) + 1):
                if num % a == 0:
                    proof.append(a)
                    break
            else:
                #print "prime in base {}".format(b)
                break
        
        if len(proof) == 9:
            print "{} {}".format(jam, " ".join(map(str, proof)))
            jamcoins += 1

        if jamcoins >= j:
            break
        i+=1
