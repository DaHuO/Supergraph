fin = open('countingsheep.in', 'r')
fout = open('countingsheep.out', 'w')

count = 0

for line in fin:
    if count != 0:
        x = int(line)
        out = None

        if x == 0:
            out = 'INSOMNIA'
        else:
            digs = {}
            y = 1
            while len(digs) < 10:
                for dig in str(x * y):
                    digs[dig] = True
                y += 1
            out = str(x * (y - 1))

        fout.write('Case #%d: %s\n' % (count, out))
    count += 1
