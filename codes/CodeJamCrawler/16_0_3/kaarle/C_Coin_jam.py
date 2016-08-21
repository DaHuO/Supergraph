# -*- coding: utf-8 -*-


from math import sqrt; from itertools import count, islice

def getDivisor(n):
    if n < 2: return 1
    for num in islice(count(2), int(sqrt(n)-1)):
        if not n%num:
            return num
    return 1
    
def getBase(str,b):
    n=0
    for i in range(len(str)):
        if str[i] == "1":
            n+=b**(len(str)-1-i)
    return n        
    

#10**15+1..10**16-1
def answer(start,size,filename):
#start = 2**15+1
#size = 50


    f=open(filename,"w+")
    result="Case #1:"
    current_size=0
    for number in islice(count(start,2),start-2):#2**15-1):
        temp=""    
        coin="{0:b}".format(number)
        temp+= coin + " "
        div2=getDivisor(number)#2
        if div2 == 1:
            continue
        else:
            temp+= str(div2) + " "
        isPass=0
        for i in range(3,10):
            div=getDivisor(int(getBase(coin,i)))
            if div == 1:
                isPass=1
                break
            else:
                temp+= str(div) + " "
        
        if isPass ==1:
            continue
       
        
        div10=getDivisor(int(coin))#10
        if div10 == 1:
            continue
        else:

            temp+= str(div10)
            result+= "\n" + temp
            current_size+=1
            print(current_size)
            
        if current_size == size:
            break
    #return result
    f.write(result)
    f.close()


#print(getBase("111",10))
#answer(getBase("1000000000110101",2),1)
answer(2**15+1,50,"result_small.txt")
answer(2**31+1,500,"result_big.txt")
#print(answer(2**15+1,50))
