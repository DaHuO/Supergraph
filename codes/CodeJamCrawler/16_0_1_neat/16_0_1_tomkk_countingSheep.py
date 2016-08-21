infile = open('sc.in', 'r')
outfile = open('countingSheepLarge.out', 'w')
iterations = infile.readline()

def countingSheep(iterations, file, outfile):
    for i in range(iterations):
        outfile.write("Case #" + str(i + 1) + ": ")
        digits = [1,2,3,4,5,6,7,8,9,0]
        digitsNew = []
        originalNumber = int(infile.readline())
        count = 0
        ketil = True
        insomnia = False
        number = originalNumber

        while(ketil or not insomnia):    
            for i in str(number):
                if int(i) in digits:
                    digitsNew.append(int(i))
                    digits.remove(int(i))

            if len(digits) == 0:
                ketil = False
                break
            else:
                count +=1 
                number = count * originalNumber        
            
            if originalNumber == (number * (count + 1)):
                insomnia = True
                break
            print(digits)
            print(number)
        if insomnia:
            outfile.write("INSOMNIA")
        else :
            outfile.write(str(number))

        if i != (iterations - 1):
            outfile.write("\n")

countingSheep(int(iterations), infile, outfile)
infile.close()
outfile.close()

