import fileinput
import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)


nTest = 0
line_no = 0
instances = []

for line in fileinput.input():
    if line_no == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    else:
        S = line.rstrip("\n\r")
        instances.append(S)
        logging.debug ("Instance: %s" % S)
    line_no+=1

a = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

b = {}
for x in a:
    for y in x:
        if y in b.keys():
            if not x in b[y]:
                b[y].append(x)
        else:
            b[y] = [x]

lists = [a]
# for x in b.keys():
#     print x, b[x]

# print

c = a
prev = []
single_seqs = []
while len(prev) != len(c):
    prev = c
    single_chars = {}
    for x in b.keys():
        if len(b[x]) == 1:
            c = [y for y in c if y != b[x][0]]    
            single_chars[x] = b[x][0]
    b = {}
    for x in c:
        for y in x:
            if y in b.keys():
                if not x in b[y]:
                    b[y].append(x)
            else:
                b[y] = [x]
    #print "c", c
    # for x in b.keys():
    #     print x, b[x]
    single_seqs.append(single_chars)

#print b, a

# for b in single_seqs:
#     print "single chars"
#     for x in b.keys():
#         print x, b[x]
#     print 

nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def instance(s):
    output = []
    b = {}
    #print s
    for x in s:
        if x in b:
            b[x] +=1
        else:
            b[x] = 1
    for s_chars in single_seqs:
        #print s_chars
        #print b
        for c in s_chars.keys():
            #print c
            while c in b.keys() and b[c] > 0:
                for y in s_chars[c]:
                    #print y, c, s_chars[c]
                    b[y] -= 1
                    assert (b[y] >=0)
                output.append(str(nums.index(s_chars[c])))

    output.sort()
    return "".join(output)
            
out_line_no = 1
for x in instances:
    result = instance(x)
    print "Case #%d: %s" % (out_line_no, instance(x))
    out_line_no+=1


