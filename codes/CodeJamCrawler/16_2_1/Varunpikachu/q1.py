tcases=int(input())
case=1

def getnumber(string):
	count=[0]*26
	res=[]
	for x in string:
		count[ord(x)-65]+=1

	while count[ord('Z')-65]>0:
		res.append(0)
		count[ord('Z')-65]-=1
		count[ord('E')-65]-=1
		count[ord('R')-65]-=1
		count[ord('O')-65]-=1
	
	while count[ord('W')-65]>0:
		res.append(2)
		count[ord('T')-65]-=1
		count[ord('W')-65]-=1
		count[ord('O')-65]-=1
	
	while count[ord('X')-65]>0:
		res.append(6)
		count[ord('S')-65]-=1
		count[ord('I')-65]-=1
		count[ord('X')-65]-=1

	while count[ord('S')-65]>0:
		res.append(7)
		count[ord('S')-65]-=1
		count[ord('E')-65]-=2
		count[ord('V')-65]-=1
		count[ord('N')-65]-=1

	while count[ord('V')-65]>0:
		res.append(5)
		count[ord('F')-65]-=1
		count[ord('I')-65]-=1
		count[ord('V')-65]-=1
		count[ord('E')-65]-=1
	#print(count,res)

	while count[ord('U')-65]>0:
		res.append(4)
		count[ord('F')-65]-=1
		count[ord('O')-65]-=1
		count[ord('U')-65]-=1
		count[ord('R')-65]-=1
	

	while count[ord('O')-65]>0:
		res.append(1)
		#print('here',res,count)
		count[ord('O')-65]-=1
		count[ord('N')-65]-=1
		count[ord('E')-65]-=1
		
	while count[ord('N')-65]>0:
		res.append(9)
		count[ord('N')-65]-=2
		count[ord('I')-65]-=1
		count[ord('E')-65]-=1

	while count[ord('G')-65]>0:
		res.append(8)
		count[ord('E')-65]-=1
		count[ord('I')-65]-=1
		count[ord('G')-65]-=1
		count[ord('H')-65]-=1
		count[ord('T')-65]-=1

	while count[ord('H')-65]>0:
		res.append(3)
		count[ord('T')-65]-=1
		count[ord('H')-65]-=1
		count[ord('R')-65]-=1
		count[ord('E')-65]-=2

	return ''.join(map(str,sorted(res)))

while case<=tcases:
	print('Case #'+str(case)+':',end=' ')
	print(getnumber(input()))
	case+=1