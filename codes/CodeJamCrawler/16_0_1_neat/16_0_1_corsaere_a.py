FILENAME = 'A-large.in'
OUTPUT = 'A-large-response.txt'
i = 0
with open(FILENAME) as f:
    with open(OUTPUT, 'w') as w:
        for line in f.readlines():
            num = int(line.strip())
            if num == 0:
                w.write("Case #{0}: INSOMNIA".format(i+1))
            else:
                pool = set()
                acc = 0
                count = 0
                while len(pool) != 10:
                    acc += num
                    for x in str(acc):
                        pool.add(x)    
                w.write("Case #{0}: {1}".format(i+1, acc))
            w.write("\n")
            i += 1 
