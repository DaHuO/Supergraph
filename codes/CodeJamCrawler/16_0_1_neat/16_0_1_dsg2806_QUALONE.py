file = open('A-large.in')
lines = file.readlines()

t = int(lines[0])

for i in range(0, int(t)):
    var = 0
    

    listNums = [0,1,2,3,4,5,6,7,8,9]
    number = lines[1 + i]
    number = number.strip()
    
    x = 0
    ogNumber = number
    if number == "0":
        var = "INSOMNIA"
        print('Case #{}: {}'.format(i+1, var))
        continue
    
    while listNums:
        x += 1
        number = int(ogNumber) * x
        ch = 0
        ch = int(ch)
        
        for ch in list(map(int, str(number))):
            try:
                listNums.remove(ch)
                var += 1
            except:
                pass
    if listNums == []:
        var = number
    
    print('Case #{}: {}'.format(i+1, var))
        

    '''
    while listNums:

        x += 1
        ch = 0
        ch = int(ch)
        for ch in list(map(int, str(x * number))):
            try:
                listNums.remove(int(ch))
                var += 1
            except:
                pass
'''
   # print('Case #{}: {}'.format(i+1, var))
'''

        z = int(z)
        number = 1234
        for z in str(number):
            print(z)
            x += 1
            for lel in str(int(z) * int(x)):
            #for each digit in int(z) * int(x) remove!
                try:
                    listNums.remove(int(lel))
                    var += 1
                except:
                    pass

'''

   
