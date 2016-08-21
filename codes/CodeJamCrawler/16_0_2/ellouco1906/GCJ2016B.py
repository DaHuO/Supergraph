#2016A-example.in
#2016A-example.out
#2016A-small-practice.in
#2016A-large-practice.in

in_file = open('2016B-large.in','r')
out_file = open('2016B-large.out','w')
num = int(in_file.readline())
print(num)
for i in range(0,num):
    dado = in_file.readline()[:-1]
    print(dado)
    result=0
    if len(dado)>1:
        for j in range(1,len(dado)):
            if dado[j] != dado[j-1]:
                result=result+1
    if dado[-1:]=='-':
        result=result+1
    d = 'Case #'+str(i+1)+': '+str(result)
    print(d)
    out_file.write(d+'\n')
out_file.close()
in_file.close()


