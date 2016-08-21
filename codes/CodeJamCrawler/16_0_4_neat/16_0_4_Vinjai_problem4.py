__author__ = 'Vinayak'


data=list()
output_data=''

with open("D-small-attempt1.in",'r') as f:
    for line in f.readlines():
        data.append(line)

test_case=int(data.pop(0))
i=0
while i<test_case:
    temp=data.pop(0).split(" ")
    K=int(temp[0])
    C=int(temp[1])
    S=int(temp[2])
    impossible=False
    tile_num_list=[]
    if C==1 and K!=S:
        impossible=True
    elif C==1 and K==S:
        tile_num_list=range(1,K+1)
    elif K==1 and K==S:
        tile_num_list=range(1,K+1)
    elif C>1:
        tile_num_list=range(2,K+1)
    tile_num_list=[str(n) for n in tile_num_list]
    if not impossible:
        output_data+="Case #"+str(i+1)+": "+" ".join(tile_num_list)+"\n"
    else:
        output_data+="Case #"+str(i+1)+": "+str("IMPOSSIBLE")+"\n"
    i=i+1

#print(output_data)
with open("outputfile1.in",'w') as f:
    f.write(output_data)