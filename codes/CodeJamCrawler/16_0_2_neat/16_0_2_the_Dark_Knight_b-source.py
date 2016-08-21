#fi=open("B-small-attempt0.in",'r')#Input File
#fo=open("B-small-attempt0.out",'w')#Output File

fi=open("B-large.in",'r')#Input File
fo=open("B-large.out","w")#Output File

#fi=open("B.in",'r')#Input File
#fo=open("B.out","w")#Output File

def reverse(stack):

	return [not s for s in stack]

def partial_reverse(stack, size):

	i = 0
	while i	< size and stack[i] != False:
		stack[i] = False
		i += 1
	return stack
		
T = int(fi.readline())
for case in range(1,T+1,1):
    ans = 0
    ############################################
    stack = [True if ch == '+' else False for ch in fi.readline().strip()]
    size = len(stack)
    
    while size > 0:
    	while size > 0 and stack[size-1] == True:
    		size -= 1
    	if size == 0:
    		break	
    	if stack[0] == False:
    		stack = reverse(stack)
    	else:		
    		stack = partial_reverse(stack, size)
    	ans += 1	
    ############################################
    fo.write("Case #%s: %s\n"%(case, ans))    
