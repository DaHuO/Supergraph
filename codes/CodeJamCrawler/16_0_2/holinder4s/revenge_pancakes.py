input_file = open("B-large.in", 'r')
output_file = open("B-large.out", 'w')
#T = int(raw_input())
T = int(input_file.readline())

def happy_check(stack):
    for i in xrange(0,len(stack)):
        if(stack[i] == '-'):
            return 0
    return 1

for i in xrange(0,T):
    #S = list(raw_input())
    S = list(input_file.readline())
    count = 0
    while(1):
        if(happy_check(S)):
            break
        else:
            start = S[0]
            if(start == '-'):
                S[0] = '+'
            else:
                S[0] = '-'
                
            for j in xrange(1,len(S)):            
                if(S[j] != start):
                    break
                else:
                    S[j] = S[0]
        count += 1
    output_file.write('Case #' + str(i+1) + ': ' + str(count) + '\n')
    #print count
input_file.close()
output_file.close()
                
