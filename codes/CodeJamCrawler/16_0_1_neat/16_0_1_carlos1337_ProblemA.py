f = open('A-large.in','r')
f2 = open('A-large.out','w')
num = 0
for line in f:
    if num == 0:
        num+=1
        continue    
    number = 0
    base_number = int(line)
    seen = [False]*10
    seenNumbers = 0
    if base_number == 0:
        number = "INSOMNIA"
    else:
        while seenNumbers < 10:
            number = number+base_number
            for char in str(number):
                if not seen[int(char)]:
                    seen[int(char)]= True
                    seenNumbers+=1            
    f2.write("Case #{0}: {1}\n".format(num,number))    
    num+=1
f.close()
f2.close()