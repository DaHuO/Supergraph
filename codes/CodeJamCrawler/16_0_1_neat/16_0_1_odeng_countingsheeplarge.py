
def countingsheep():

    fname = 'A-large.in'
    content = []
    with open(fname) as o:
        for line in o:
            content.append(int(line))
    
    print(content)
    x=False
    content=content[1:]
    print(len(content))

    for a, n in enumerate(content):
        output = getoutput(n)
        f = open('output.out', 'a')
        f.write('Case #' + str(a+1) + ': ' + output + '\n')
        f.close()
        
        



def getoutput(n):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1, 1000001):
        temp = str(i*n)
        # print(temp)
        for digit in temp:
            d = int(digit)
            if d in digits:
                digits.remove(d)
                print(digits)
                if not digits:
                    return temp
                
        if digits and i == 1000000:
            return 'INSOMNIA\n'

            
countingsheep()
