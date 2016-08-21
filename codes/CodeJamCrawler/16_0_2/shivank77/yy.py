def reverse(string):
    #string = string[::-1]
    string = string.replace('-','=')
    string = string.replace('+','-')
    string = string.replace('=','+')
    return string

t = int(input())
for i in range(1,t+1):
    string = input()
    p = len(string)
    s = ''
    count = 0
    c = 0
    if string == '+'*p:
        print("Case #{}: {}".format(i, 0))
    elif string=='-'*p:
        print("Case #{}: {}".format(i, 1))
    else :      
        while len(string)>0:
            if string[-1]=='+':                
                string = string[:-1]                   
            else :
                string = reverse(string)
                count += 1
        print("Case #{}: {}".format(i, count))

