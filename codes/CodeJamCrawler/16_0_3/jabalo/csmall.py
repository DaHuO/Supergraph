import math
f = open('/Users/jacquelineabalo/Documents/C-small-attempt1.in');
lines = f.readlines();
target = open('/Users/jacquelineabalo/Documents/csmallresult.txt', 'w');
target.write('Case #1: \n');
nu = lines[1].strip().split(' ');
N = int(nu[0]);
J = int(nu[1]);
strNumber = '1';
x = 0;
while (x<N-2):
    strNumber = strNumber + '0';
    x = x + 1;
strNumber+='1';
   
for i in range(1, J+1):
    total = 0;
    while total!=9:
        factors = strNumber;
        for j in range(2,11):
            intNumber = int(strNumber,j);
            found = 0;
            divisor = 2;
            while divisor<math.sqrt(intNumber):               
                if intNumber%divisor==0:
                    factors = factors + ' ' + str(divisor);
                    found = 1;
                    total = total + 1;
                    break;
                else:
                    divisor = divisor + 1;
            if not found:
                total = 0;
                break;
        while True:
            inner = strNumber[1:-1];
            inner = bin(1+int(inner,2))[2:];
            while len(inner)!=(N-2):               
                inner = '0' + inner;
            strNumber = '1' + inner + '1';
            if len(strNumber)==N and strNumber[0]=='1' and strNumber[-1]=='1':
                break;
    target.write(factors + '\n');
    if i!=J:
        while True:
            inner = strNumber[1:-1];
            inner = bin(1+int(inner,2))[2:];
            while len(inner)!=(N-2):
                inner = '0' + inner;
            strNumber = '1' + inner + '1';           
            if len(strNumber)==N and strNumber[0]=='1' and strNumber[-1]=='1':
                break;
target.close();
f.close();
print('done');
           
        
    
