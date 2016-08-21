from array import array
data = open('A-large.in','r')
d = open('A-large.out','w')

cases = data.readline()
cases = int(cases)

case_count = 1

while (case_count <= cases):
    N = data.readline()
    N = int(N)

    checker = 1
    done = 0
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0
    d7 = 0
    d8 = 0
    d9 = 0
    d0 = 0
    print(N)
    while(done == 0):

        val = N*checker

        values = [int(i) for i in str(val)]
        #values = int(values)

        ans = len(values)
        counter = 0
        #print (values, ans)

        while (counter < ans):
            #print(d0)
            if( values[counter] == 1):
                d1 = 1
            elif( values[counter] == 2):
                d2 = 1
            elif( values[counter] == 3):
                d3 = 1
            elif( values[counter] == 4):
                d4 = 1
            elif( values[counter] == 5):
                d5 = 1
            elif( values[counter] == 6):
                d6 = 1
            elif( values[counter] == 7):
                d7 = 1
            elif( values[counter] == 8):
                d8 = 1
            elif( values[counter] == 9):
                d9 = 1
            elif( values[counter] == 0):
                d0 = 1

            counter += 1

        sleep = d1+d2+d3+d4+d5+d6+d7+d8+d9+d0
        
        if (sleep == 10):
            done = 1
            print('Case #' + str(case_count) + ': ' + str(val), file = d)
        if (val == 0):
            done = 1
            print('Case #' + str(case_count) + ': ' + 'INSOMNIA', file = d)

        checker += 1

    case_count += 1

d.close()

        
