t = input()
least_manv=1000000
new_list=[]
new_dict={}

def flipstr(cur_str,till):
    temp_str=list(cur_str)
    if till>0:
        new_str_list=temp_str[:till]
        for i in range(till):
            if new_str_list[i]=='-':
                new_str_list[i]='+'
            else:
                new_str_list[i]='-'
        new_str_list.reverse()
        for i in range(till):
            temp_str[i]=new_str_list[i]
    
    return temp_str

def recur(cur_str,manv,start):
    global least_manv,new_dict
    if manv>10:
        return
    #print cur_str
    if '+' not in cur_str:
        if least_manv>manv+1:
            least_manv=manv+1
    elif '-' in cur_str:
        try:
            if new_dict["".join(cur_str)] > manv:
                new_dict["".join(cur_str)]=manv
                for i in range(start,len(cur_str)):
                    newcur_str=flipstr(cur_str,i+1)
                    recur(newcur_str,manv+1,start+1)
        except:
            new_dict["".join(cur_str)]=manv
            for i in range(start,len(cur_str)):
                newcur_str=flipstr(cur_str,i+1)
                recur(newcur_str,manv+1,start+1)
               
    else:
        if least_manv>manv:
            least_manv=manv

ans=[]

for _ in range(t):
    print _
    new_dict={}
    least_manv=1000000
    inp_str=raw_input()
    inp_str=list(inp_str)
    recur(inp_str,0,0)
    out_str="Case #"+str(_+1)+": "+str(least_manv)
    ans.append(out_str)

fp = open("out.txt","w")
for i in ans:
    fp.write(str(i)+"\n")
fp.close()
