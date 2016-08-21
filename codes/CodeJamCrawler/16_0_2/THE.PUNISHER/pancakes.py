def flip(str):
    str=str[::-1]
    return ''.join('-' if x == '+' else '+' for x in str)

def found(str):
    if str == ('+'*len(str)):
        return True
    return False

def position(str):
    i = len(str)
    for c in reversed(str):
        if c=='-':
            return i
        i-=1

def func(line):
    plus_found = False
    minus_found = False
    plus_index = 0
    minus_index = 0
    num=0
    if(found(line)):
            return num
    for i in range(len(line)):
        if line[i]=='+':
            if minus_found==True and plus_found==True :
                flipped=flip(line[:plus_index+1])+line[plus_index+1:]
                line=flip(flipped[:minus_index+1])+flipped[minus_index+1:]
                num+=2
                minus_found=False
            elif minus_found==True:
                line=flip(line[:minus_index+1])+line[minus_index+1:]
                num+=1
                minus_found=False
            plus_found = True
            plus_index=i
        else:
            minus_found = True
            minus_index=i
        if(found(line)):
            return num
    if minus_found==True and plus_found == False:
        line = flip(line)
        num+=1
    elif minus_found==True and plus_found == True:
        flipped=flip(line[:plus_index+1])+line[plus_index+1:]
        line=flip(flipped[:minus_index+1]+flipped[minus_index+1:])
        num+=2
    return num

lines = [line.rstrip('\n') for line in open('in_pancake')]
i=1
for line in lines[1:len(lines)]:
    print 'Case #'+str(i)+':',func(line)
    i+=1