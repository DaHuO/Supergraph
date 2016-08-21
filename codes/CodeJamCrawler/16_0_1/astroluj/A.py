
inputFile = open ('A-large.in', 'r')
outputFile = open('output.txt', 'w')

line = int(inputFile.readline())
for i in range(line):
    x = int(inputFile.readline())

    if not x:
        answer = 'INSOMNIA'
    else:
        intArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        orgNum = num = x
        while intArray:
            while x:
                mod = int(x % 10)
                x = int(x / 10)

                try:
                    intArray.remove(mod)
                except ValueError as e:
                    pass
                if not intArray: break
            else: num = x = num + orgNum
     
        answer = num

    outputFile.write('Case #{0}: {1}\n'.format((i + 1), answer))


    
inputFile.close()
outputFile.close()
