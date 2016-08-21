'''
Algorithm
---------
Repeat:
    if string start with + then find the occurence of next -. Then flip the
    the string before that -

    if string start with - then find the occurence of next +. Then flip the
    the string before that +
'''

def flip(pos):
    global cakes
    for i in range(pos+1):
        if(cakes[i]=='+'):
            cakes[i]='-'
        elif(cakes[i]=='-'):
            cakes[i]='+'
    temp = cakes
    for i in range(pos+1):
        cakes[i] = temp[pos-i]
    return



f = open('E:\\Code Jam 2016\\Revenge of the Pancakes\\B-large.txt', mode = 'r')
fo = open('E:\\Code Jam 2016\\Revenge of the Pancakes\\out.txt', mode = 'w')

testCases = int(f.readline())

for case in range(1,testCases+1):
    cakes = list(f.readline())
    if(cakes[len(cakes)-1]=='\n'):
        cakes.remove('\n')
    flips = 0
    #print 'Cakes = ',cakes
    while(True):

        if(cakes[0]=='+'):
            for i in range(0,len(cakes)):
                if(cakes[i] == '-'):
                    #print 'Flipping1 till ',i-1
                    flip(i-1)
                    flips = flips + 1
                    #print cakes
                    break

        elif(cakes[0]=='-'):
            for i in range(len(cakes)):
                if(cakes[i] == '+' or i==len(cakes)-1):
                    if(len(cakes)==1):
                        #print 'Flipping2 till ',i
                        flip(i)
                        flips = flips + 1
                        #print cakes
                        break
                    elif(i==len(cakes)-1 and cakes[i]=='-'):
                        #print 'Flipping3 till ',i
                        flip(i)
                        flips = flips + 1
                        #print cakes
                        break
                    else:
                        #print 'Flipping4 till ',i-1
                        flip(i-1)
                        flips = flips + 1
                        #print cakes
                        break

        if(not('-' in cakes)):
            print 'Case ',case,' complete in streps '+str(flips)
            output = 'case #'+str(case)+': '+str(flips)+'\n'
            fo.writelines(output)
            break
