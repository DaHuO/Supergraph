#2016A-example.in
#2016A-example.out
#2016A-small-practice.in
#2016A-large-practice.in

in_file = open('2016A-large.in','r')
out_file = open('2016A-large.out','w')
num = int(in_file.readline())
print(num)
for i in range(0,num):
    cases=['0','1','2','3','4','5','6','7','8','9']
    dado = int(in_file.readline())
    print(dado)
    if dado==0:
        d = 'Case #'+str(i+1)+': '+'INSOMNIA'
    else:
        k=1
        while True:
            valor=k*dado
            for digit in str(valor):
                if digit in cases:
                    cases.remove(digit)
            if len(cases)==0:
                break
            k=k+1
        if len(cases)>0:
            d = 'Case #'+str(i+1)+': '+'INSOMNIA'
        else:    
            d = 'Case #'+str(i+1)+': '+str(valor)
    print(d)
    out_file.write(d+'\n')
out_file.close()
in_file.close()


