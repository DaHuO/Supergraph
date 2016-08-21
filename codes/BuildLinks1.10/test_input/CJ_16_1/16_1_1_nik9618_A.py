def solve(str):
	if(len(str)==0):
		return ""
	answer = str[0]
	for i in range(1,len(str)):
		if(str[i]>=answer[0]):
			answer = str[i] + answer
		else:
			answer+=str[i]
	return answer

i = 1
with open('/Users/nik9618/Downloads/A-large.in') as f:
    lines = f.readline()
    lines = f.readlines()
    for l in lines:
    	print "CASE #"+str(i)+":",solve(l.split("\n")[0])
    	i+=1
