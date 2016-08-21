file = open("A-large.in","r")
contents = file.readlines()
number_of_lines = contents[0].strip()
lines = [int(contents[i].strip()) for i in range(1,int(number_of_lines)+1)]
file.close()
results=[]

def reset_dic():
    dic_template = {}
    for x in "0123456789":
        dic_template[x]=0
    return dic_template

dic = reset_dic()

for i in lines:
    if i==0:
        results.append("INSOMNIA")
    else:
        n=1
        while 0 in dic.values():
            for digit in str(i*n):
                dic[digit]=1
            n+=1
        results.append(i*(n-1))
        dic=reset_dic()



file=open("A-large.out","w")
for a in range(len(results)):
    file.write("Case #{0}: {1}\n".format(a+1,results[a]))
file.close()
        
