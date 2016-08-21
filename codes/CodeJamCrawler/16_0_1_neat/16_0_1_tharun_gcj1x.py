in_file = '/home/tharun/Desktop/input.txt'
out_file = '/home/tharun/Desktop/output.txt'
target = open(out_file, 'w')
with open(in_file, "r") as f:
    content = f.read().splitlines()
    tc = int(content[0])
    sleep = '1111111111'
    for i in xrange(1,tc+1):
        valst = content[i]
        val = int(valst)
        current = bytearray('0000000000')
        k = 1
        if valst == '0':
            line = 'Case #%d: INSOMNIA' % i
            target.write(line)
            target.write("\n")
            continue
        while k > 0:
            num = k * val
            # print k,val,num
            numst = str(num)
            length = len(numst)
            for j in xrange(0,length):
                index = int(numst[j])
                current[index] = '1'
            if current == sleep:
                line = 'Case #%d: %d' % (i,num)
                target.write(line)
                target.write("\n")
                break
            k = k + 1

