import math

def interpretnum(start, base):
    total = 0

    multiplier = 0
    for char in (start)[::-1]:
        total += int(char)*math.pow(base, multiplier)
        multiplier += 1
  
    return int(total)

boo = 0
answers = []
primes = [2,3]

with open('coininput.txt', 'r') as fi:
    for line in fi:
        if boo == 0:
            boo = 1
            continue

        vals = line.split()
        #print vals

        n = int(vals[0])
        j = int(vals[1])

        start = int(math.pow(2, n-1) + 1)
        
        p = 5
        while (primes[-1] < 1000000):#1+int(math.sqrt(math.pow(10, n-2)))):
            for prime in primes:
                if prime>math.sqrt(p):
                    primes.append(p)
                    p+=2
                    break
                if p%prime == 0:
                    p+=2
                    break

        i = 0
        while (len(answers) < j and start < int(math.pow(2, n))):
            skip = 0
            factors = []

            base = 2
            while (base <= 10):
                if skip:
                    break

                i = interpretnum(bin(start)[2:], base)

                for p in primes:#Finds first p that divides i
                    if p > math.sqrt(i):
                        skip = 1
                        break
                    if i%p == 0:
                        factors.append(p)
                        break
                    if p == primes[-1]:
                        skip = 1
                base += 1
            
            if len(factors) == 9:
                ans = bin(start)[2:]
                for fact in factors:
                    ans = ans + ' ' + str(fact)
                answers.append(ans)

            start += 2

    fi.close

val = 1
with open('coinoutput.txt', 'a') as fi:
    fi.write('Case #' + str(val) + ':' + '\n')
    for answer in answers:
        fi.write(str(answer) + '\n')
    fi.close
