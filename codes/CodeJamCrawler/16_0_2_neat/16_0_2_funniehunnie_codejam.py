case = int(input())
for a in range(case):
    answer = 0
    string = input().strip()
    array = list(string)
    #print(array)
    while string != len(string) * '+':
        index = 0
        answer += 1
        if array[0] == '+':
            while index < len(string) and array[index] == '+':
                array[index] = '-'
                index += 1
            string = ''.join(array)
            #print(array)
        else:
            array.reverse()
            tempString = ''.join(array)
            newString = ''
            numPlus = 0
            switch = 0
            for i in tempString:
                if switch == 0:
                    if i == '-':
                        switch = 1
                        newString += '+'
                    else:
                        numPlus += 1
                else:
                    if i == '-':
                        newString += '+'
                    else:
                        newString += '-'
            newString += numPlus * '+'
            string = newString
            array = list(newString)
            '''
            print(1, string)
            print(array)
            
        if answer == 30:
            break
            '''
    print("Case #%i: %i" %(a + 1, answer))
