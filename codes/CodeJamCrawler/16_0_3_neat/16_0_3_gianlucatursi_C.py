def factors(n):
    frac = reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    frac.remove(1)
    frac.remove(n)
    return frac

def bin_add(*args):
    val = bin(sum(int(x, 2) for x in args))[2:]
    if val[-1:] == '0':
        return bin_add(val, "1")
    return val

def exC(N, J):

    results = []
    inter = [0]*(N-2)
    string = "1" + ''.join([str(x) for x in inter]) + "1"

    while len(results) < J:

        setDivisor = []
        done = False

        while not done:
            for base in range(2,11):

                value = int(string, base)
                #print value
                divisor = factors(value)
                if len(divisor) == 0:
                    done = True
                else:
                    setDivisor.append(divisor[0])

            #print setDivisor

            if len(setDivisor) == 9:
                done = True

        results.append({"string": string, "divisor": setDivisor})
        string = bin_add(string, "1")
        #print "**********"
        #print results
        #print "**********"
    return results



with open('input_small.txt','r') as reader:
    next(reader)
    case = 0
    for line in reader:
        values = line.replace('\n', '').split(' ')
        res = exC(int(values[0]), int(values[1]))
        case += 1
        print "Case #"+ str(case) +":"
        for r in res:
            print (r['string'] + " " + ''.join([str(x) + ' ' for x in r['divisor']]))[:-1]
