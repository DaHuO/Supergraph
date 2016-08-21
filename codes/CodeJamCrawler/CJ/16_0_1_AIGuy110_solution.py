infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

cases = int( infile.readline())
for case in range(1, cases+1):
        N = int( infile.readline())
        if N == 0:
                outfile.write('Case #'+str(case)+': INSOMNIA\n')	
                continue

        seenDigs = []
        x = 1
        while True:
                numStr = str( N*x )
                for dig in numStr:
                        if not dig in seenDigs:
                                seenDigs.append(dig)
        
                if len(seenDigs) == 10:
                        outfile.write('Case #'+str(case)+': '+numStr+'\n')
                        break

                x += 1

infile.close()
outfile.close()
