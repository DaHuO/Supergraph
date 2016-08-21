file = open("D-small-attempt2.in", 'r')
outfile = open("fractilesOUT.txt", 'w')
cases = int(file.readline())
##lines = file.readlines()
##for i in range(len(lines)):
##    print("Case #" + str(i+1) + ' ' + str(lines[i]))

for i in range(cases):
    line = file.readline().split(' ')
    tiles = int(line[0])
    sets = int(line[1])
    students = int(line[2])

    outfile.write("Case #" + str(i+1) + ": ")
    if students < tiles:
        print("HEY")
        outfile.write("IMPOSSIBLE")
    else:
        if sets == 1:
            if students == tiles:
                for i in range(1,students+1):
                    outfile.write(str(i))
                    if i != students:
                        outfile.write(' ')
        else:
            if students == 1 and tiles == 1:
                for i in range(1,students+1):
                    outfile.write(str(i))
                    if i != students:
                        outfile.write(' ')
            elif tiles == 2 and sets > 1:
                outfile.write(str(tiles))
            else:
                if tiles - 1 < students:
                    arr = []
                    count = 0
                    for num in range(tiles - 1):                
                        outfile.write(str(2+count))
                        count = count + tiles + 1
                        if num != tiles - 2:
                            outfile.write(' ')
                else:
                    outfile.write("IMPOSSIBLE")
                    
    if i != cases - 1:
        outfile.write('\n')
    
file.close()
outfile.close()         
            
