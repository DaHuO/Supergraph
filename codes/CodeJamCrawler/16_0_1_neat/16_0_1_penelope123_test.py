# import random

f = open('A-large.in')
length = int(f.readline())
numbers = [int(f.readline()) for i in range(length)]

# i = -1
# while True:
#     i += 1
#     n = random.randrange(10**6)
#     print "number is ", n

for i, n in enumerate(numbers):
    remaining = ['1','2','3','4','5','6','7','8','9','0']
    count = 1
    if n == 0:
        print "Case #%s: INSOMNIA" % (i+1)
        continue
    while True:
        num = n*count
        found = []
        for r in remaining:
            if r in str(num):
                found.append(r)
        for r in found:
            remaining.remove(r)
        if not remaining:
            break
        count += 1
        if count > 1000:
            print "expected death"
            exit()
    print "Case #%s: %s" % (i+1, num)
