def countingsheep():
    fname = 'A-small-attempt1.in'
    content = []
    with open(fname) as o:
        for line in o:
            content.append(int(line))
    
    print(content)
    x=False
    content=content[1:]
    print(len(content))
    
    for a, n in enumerate(content):
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(1, 201):
            temp = str(i*n)
            # print(temp)
            for digit in temp:
                d = int(digit)
                if d in digits:
                    digits.remove(d)
                    print(digits)
                    if not digits:
                        f = open('output.out', 'a')
                        f.write('Case #' + str(a+1) + ': ' + temp + '\n')
                        f.close()
                        x = True
                        break
    
            if digits and i == 200:
                print(i)
                f = open('output.out', 'a')
                f.write('Case #' + str(a+1) + ': ' +'INSOMNIA\n')
                f.close()
     
            
countingsheep()
