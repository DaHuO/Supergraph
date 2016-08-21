import math

def bin_generator(length):
    for i in xrange(0, 2<<(length-3)):
        yield (i << 1 | 2<<(length-2) | 1)

def isPrimeDeter(num):
    if num == 2:
        return None, True
    if num <= 1:
        return None, False

    sqr = int(math.sqrt(num)) + 1
    count = 0
    for divisor in xrange(3, sqr, 2):
        if (num % divisor) == 0:
            return divisor, False
        elif count >= 200:
            return None, True
        count +=1
    return None, True




def jamcoins(settings):
    length, probs = [int(a_setting) for a_setting in settings.split(" ")]
    domain = []
    """
    0101 & 2*3 == 0 not in domain
    1000 & 2*3 == 1

    """
    for i in bin_generator(length):
        divisors = []
        for x in range(2,11):
            number = int(bin(i).replace("0b",""), x)
            if (number % 10) in [7]:
                break
            divisor, is_prime = isPrimeDeter(number)
            if is_prime:
                break
            else:
                divisors.append(divisor)
            if x == 10:
                domain.append((bin(i), divisors))
        if len(domain) == probs:
            break
    output = ''
    for entry in domain:
        output += str(entry[0]).replace("0b","")
        output += " " + " ".join([str(div) for div in entry[1]])
        output += "\n"
    return output
def inputDissect(s):
    lines = s.split("\n")
    inputCnt = int(lines.pop(0))
    for offset in xrange(inputCnt):
        y = jamcoins(lines[offset])
        print "Case #%d:\n" % (offset + 1), y

inp = """1
32 500"""


#print isPrimeDeter(3)
#print isPrimeDeter(5)
#print isPrimeDeter(7)
#print isPrimeDeter(55)
inputDissect(inp)
