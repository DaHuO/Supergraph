inputfile = open('inputfile.txt', 'r')
outputfile = open('outputfile.txt', 'w')

for num, line in enumerate(inputfile,1):
    if (num > 1):
        numlist = [0,1,2,3,4,5,6,7,8,9]
        N0 = int(line)
        for i in range(1, 1000):
            N= N0*i
#            print N
            for char in str(N):
                if (numlist.count(int(char)) > 0):
                    numlist.remove(int(char))
                if (numlist == []):
                    break
            if(numlist == []):
                outputfile.write('Case #'+ str((num -1)) + ': ' + str(N) + '\n')
                break
            if(i == 999):
                outputfile.write('Case #'+ str((num -1)) + ': ' + 'INSOMNIA' + '\n')
                break
                    

inputfile.close()
outputfile.close()
