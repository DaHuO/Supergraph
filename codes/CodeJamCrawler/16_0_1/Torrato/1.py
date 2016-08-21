def give_no(no,store):
	while(no!=0):
		r=no%10
		no=no/10
		store[r]=1
def get_result(no):
	store=[0,0,0,0,0,0,0,0,0,0]
	i=1
	if(no==0):
		return "INSOMNIA"
	while(i<=1000000):
		give_no(no*i,store)
		if(store[0]==1 and store[1]==1 and store[2]==1 and store[3]==1 and store[4]==1 and store[5]==1 and store[6]==1 and store[7]==1 and store[8]==1 and store[9]==1):
			break;
		i=i+1;
	return str(no*i)

inp=open("input.in","r")
op=open("ouput.txt","w");
no=int(inp.readline())
i=1
while(no):
	str1=get_result(int(inp.readline()));
	str1="Case #"+str(i)+": "+str1
	op.write(str1);
	op.write("\n")
	no=no-1
	i=i+1;
op.close()
inp.close()

