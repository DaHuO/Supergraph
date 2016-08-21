



def calcu(Input1):
    Input2 = Input1.replace('-','0')
    Input = Input2.replace('+','1')

    Loop = 0
    Number = 0
    while Loop == 0:
        if Input.find('1') != -1 and Input.index('1') != 0:
            Input = Input[Input.index('1'):] + Input[:Input.index('1')].replace('0','1')
            Number = Number + 1
            if Input.find('0') != -1 and Input.find('0') != 0:
                Input = Input[:Input.index('0')].replace('1','0') + Input[Input.index('0'):]
                Number = Number + 1
            else:
                k = 0
        else:
            if Input.find('0') != -1 and Input.find('0') != 0:
                Input = Input[:Input.index('0')].replace('1','0') + Input[Input.index('0'):]
                Number = Number + 1
                if Input.find('1') != -1 and Input.index('1') != 0:
                    Input = Input[Input.index('1'):] + Input[:Input.index('1')].replace('0','1')        
                    Number = Number + 1

        if '1' in Input:
            hi = 0
        else:
            Input = Input.replace("0","1")
            Number = Number + 1

        if '0' in Input:
            m = 0
        else:
            Loop = 1


    return Number



if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())

    for case in range(1,T+1):
            for x in f.readline().split():
                    Input1 = str(x)
                    answer = calcu(Input1)
                    print("Case #{0}: {1}".format(case, answer)) 

    
    
            


        
    
    
    
    
