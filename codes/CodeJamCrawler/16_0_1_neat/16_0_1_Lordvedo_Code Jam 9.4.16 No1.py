def calculate(number1):
    digitSet=[]
#print(len(digitSet))
    i=1
    if number1==0:
        return 'INSOMNIA'
    else:
        while len(digitSet)<10:
            numberNew = number1*i
        #print (numberNew)
            a = set(str(numberNew))
        #print (digitSet)
        #print(set(digitSet)|(a))
            digitSet=list(set(digitSet)|(a))
            i+=1
        return numberNew
j=1
f = open('C:/Users/Vedat/Desktop/VAK/Python/A-large.in','r')
line=f.readline()

while line:
    print('Case #'+str(j-1)+': '+ str(calculate (int(line))))
    line=f.readline()
    j+=1
