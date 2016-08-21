g_list = [0] * 10
numbers = ['0','1','2','3','4','5','6','7','8','9']

def remove(S,substr,g_i):
	for c in substr:
		pos = S.index(c)
		S=S[:pos] + S[pos+1:]
	g_list[g_i]+=1
	return S
		
def compute(S):
	while 'Z' in S:
		S=remove(S,'ZERO',0)
	while 'X' in S:
		S=remove(S,'SIX',6)
	while 'S' in S:
		S=remove(S,'SEVEN',7)
	while 'G' in S:
		S=remove(S,'EIGHT',8)
	while 'H' in S:
		S=remove(S,'THREE',3)
	while 'V' in S:
		S=remove(S,'FIVE',5)
	while 'F' in S:
		S=remove(S,'FOUR',4)
	while 'W' in S:
		S=remove(S,'TWO',2)
	while 'O' in S:
		S=remove(S,'ONE',1)
	while 'N' in S:
		S=remove(S,'NINE',9)

	result = ''
	for i in range(10):
		if 0!=g_list[i]:
			result += numbers[i]*g_list[i]
	return result

if __name__ == '__main__':
	input = open('input.txt','r')
	output = open('output.txt','w')

	T = int(input.readline())
	for i in range(1,T+1):
		g_list = [0] * 10
		S = input.readline()
		result = compute(S)
		output.write('Case #{}: {}\n'.format(i,result))
	

