def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return i
    return 1

    
out1 = open('jam.out', 'w')

n = 16
m = 50

jam = 0b1000000000000001

out1.write("Case #1:\n")

while m>0:
    div = []
    for i in range(0,9):
        k = jam
        number = 0
        j = 1
        while k>0:
            number += (k % 2)*j
            #print bin(k).replace('0b',''),number
            k /= 2
            j *= (i+2)
        #print number,bin(jam), jam,i
        
        temp = isPrime(number)
        if temp == 1:
            
            break
        div.append(temp)
    if len(div) == 9:
        m -= 1
        
        out1.write("%s" %(bin(jam).replace('0b','')))
        
        for i in range(0,9):
            out1.write(" %d" %(div[i]))
        out1.write("\n")
    jam += 2

out1.close();
        
            
