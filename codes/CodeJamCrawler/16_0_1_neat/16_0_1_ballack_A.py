import sys, re, math

def digit (number):
    ret = []
    while number > 0:
        ret.append(number % 10)
        number /= 10
    return ret

if __name__ == "__main__":
    total = int(raw_input())
    for counter in xrange(1, total+1):
        counts = [0] * 10
        number = int(raw_input())
        if number == 0:
            print "Case #{}: INSOMNIA".format(counter)
            continue
        for multiplier in xrange(1, int(1e6)):
            for item in digit(multiplier * number):
                counts[item] += 1
            if all([item > 0 for item in counts]):
                break
        print "Case #{}: {}".format(counter, multiplier * number)
