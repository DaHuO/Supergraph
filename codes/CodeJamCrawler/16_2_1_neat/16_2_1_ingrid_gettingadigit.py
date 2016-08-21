
lines = open('A-small-attempt1.in', 'r')
output = open('output.txt', 'w')

numbers = range(0,10)
for i, line in enumerate(lines):
    d = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    if i > 0:
        zero = line.count('Z')
        d[0] = zero
        two = line.count('W')
        d[2] = two
        six = line.count('X')
        d[6] = six
        eight = line.count('G')
        d[8] = eight
        four = line.count('U')
        d[4] = four
        one = line.count('O') - two - zero - four
        d[1] = one
        five = line.count('F') - four
        d[5] = five
        seven = line.count('V') - five
        d[7] = seven
        nine = (line.count('N') - seven - one)/2
        d[9] = nine
        three = line.count('H') - eight
        d[3] = three
        out =  "Case #"+str(i)+": "+''.join([''.join([str(i)]*x) for i,x in d.items() if x!=0])+"\n"
        print out
        output.write(out)
#         print ''.join(reversed(sorted(line.strip("\n"))))
#         print line.strip("\n")
output.close()
