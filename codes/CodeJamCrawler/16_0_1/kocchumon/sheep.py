t = input()
ans=[]
for _ in xrange(t):
    v = input()
    out_str=""
    all_nums=[ 0 for i in range(10)]
    for i in list(str(v)):
        all_nums[int(i)]=1
    tot_attemps=1
    curr_num=0
    while 0 in all_nums and tot_attemps<=100:
        curr_num=tot_attemps*v
        tot_attemps=tot_attemps+1
        new_list=list(str(curr_num))
        for i in new_list:
            all_nums[int(i)]=all_nums[int(i)]+1

    out_str="Case #"+str(_+1)+": "
    if 0 in all_nums:
        out_str=out_str+"INSOMNIA"
    else:
        out_str=out_str+str(curr_num)

    ans.append(out_str)
        
fp=open("out.txt","w")
for i in ans:
    fp.write(i+"\n")
fp.close()
