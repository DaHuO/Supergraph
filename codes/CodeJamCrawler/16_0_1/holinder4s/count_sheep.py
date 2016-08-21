input_file = open("A-large.in", 'r')
output_file = open("A-large.out", 'w')
T = int(input_file.readline())
ten = []

def ten_check():
    for i in xrange(0,10):
        if(ten[i] == 0):
            return 0
    return 1

def ten_clear():
    for i in xrange(0,10):
        ten[i] = 0

for i in xrange(0,10):
    ten.append(0)
    
for i in xrange(0,T):
    N = int(input_file.readline())
    count = 1
    ten_clear()
    if(N==0):
        output_file.write('Case #' + str(i+1) + ': INSOMNIA\n')
        print 'Case #' + str(i+1) + ': INSOMNIA'
    else:
        while(1):
            tmp = str(count*N)
            #print tmp
            for j in xrange(0,len(tmp)):
                if(ten[int(tmp[j])] == 0):
                    ten[int(tmp[j])] = 1
            #print ten
            if(ten_check()):
                output_file.write('Case #' + str(i+1) + ': ' + str(count*N)+'\n')
                print 'Case #' + str(i+1) + ': ' + str(count*N)
                break
            count += 1

input_file.close()
output_file.close()
