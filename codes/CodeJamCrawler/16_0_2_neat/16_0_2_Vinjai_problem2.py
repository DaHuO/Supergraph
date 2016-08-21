__author__ = 'Vinayak'

def swap(str,index):
    ch_list=[]
    for ch in str[:index+1]:
        if ch == "+":
            ch_list.append("-")
        else:
            ch_list.append("+")
    for ch in str[index+1:]:
        ch_list.append(ch)
    str="".join(ch_list)
    #print(str)
    return str

data=list()
output_data=''

with open("B-large.in",'r') as f:
    for line in f.readlines():
        data.append(line)


test_case=int(data.pop(0))
i=0
while i<test_case:
    seq=data.pop(0)
    j=0
    while True:
        temp=seq.rfind("-")
        #print(temp)
        #print(seq)
        if temp==-1:
            output_data+="Case #"+str(i+1)+": "+str(j)+"\n"
            break
        else:
            seq=swap(seq,temp)
        j=j+1
    i=i+1

#print(output_data)
with open("outputfile.in",'w') as f:
    f.write(output_data)