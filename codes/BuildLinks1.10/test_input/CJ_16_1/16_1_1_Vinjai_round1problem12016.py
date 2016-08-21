__author__ = 'Vinayak'


def get_letters(N):
    return [ch for ch in N]

data=list()
output_data=''

with open("A-large.in",'r') as f:
    for line in f.readlines():
        data.append(line)

test_case=int(data.pop(0))
i=0
while i<test_case:
    N=data.pop(0).replace("\n","")
    letters=get_letters(N)
    string=letters[0]
    length=len(letters)
    j=1
    while j<length:
        curr=letters[j]
        if curr<string[0]:
            string=string+curr
        else:
            string=curr+string
        j=j+1
    output_data+="Case #"+str(i+1)+": "+string+"\n"
    i=i+1

print(output_data)
with open("outputfile.in",'w') as f:
    f.write(output_data)