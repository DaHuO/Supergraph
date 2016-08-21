inp_file=open('hello.in','r')
out_file=open('lwor.out','w')
tesctcases=int(inp_file.readline().strip())
for t in range(tesctcases):
    string=inp_file.readline().strip()
    answer=string[0]
    for i in range(1,len(string)):
        if(string[i]>=answer[0]):
            answer=string[i]+answer
        else:
            answer=answer+string[i]
    out_file.write("Case #"+str(t+1)+": "+answer+"\n")
