inputfile = open('inputfile.txt', 'r')
outputfile = open('outputfile.txt', 'w')

for num, line in enumerate(inputfile,1):
    if (num > 1):
        segcount = 0
        currentcake = ' '
        for char in line:
#            print 'char = ' + char + ' currentcake = ' + currentcake
            if char != currentcake and char != '\n':
                currentcake = char
##                if(currentcake == '+'):
##                    currentcake = '-'
##                else:
##                    currentcake = '+'
                segcount = segcount + 1
        if(currentcake == '+' and segcount >0):
            segcount = segcount - 1
        outputfile.write('Case #'+ str((num -1)) + ': ' + str(segcount) + '\n')
#        print segcount

inputfile.close()
outputfile.close()
        
                
