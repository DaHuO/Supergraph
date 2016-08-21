import sys
in_file = open("test.txt")
#in_file = sys.stdin




def merge(A, B):
    return [x or y for x,y in zip(A,B)]

def get_digits(num):
    lister = [0 for z in range(10)]

    while num:
        lister[num % 10] = 1
        num /= 10

    return lister


def cycles(num):
    lister = [0 for z in range(10)]

    cur = num
    cycles = 0
    while cycles < 100000:
        cycles += 1
        if sum(lister) == 10:
            return cur - num
            break
        lister = merge(lister, get_digits(cur))
        cur += num

    if cycles >= 100000:
        print "TOO MUCH FOR", num

    return -1

data = map(int, in_file.read().strip().split() )[1:]

#out_file = sys.stdout
out_file = open("OUTPUT.txt", 'w')

for i in range(len(data)):

    ans = ""
    if data[i] == 0:
        ans = 'INSOMNIA'
    else:
        ans = str(cycles(data[i]))

    out_file.write("Case #%i: %s\n" %(i+1, ans) )



