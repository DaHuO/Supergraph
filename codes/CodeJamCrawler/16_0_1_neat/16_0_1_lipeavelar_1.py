# -*- UTF-8 -*-

def return_list_elements(l):
	for i in l:
		yield i

if __name__ == "__main__":
	T = int(input())
	for t in range(T):
		N = int(input())
		numbers = set(['1','2','3','4','5','6','7','8','9','0'])
		seem_numbers = set()
		ans = 'Case #'+str(t+1)+': '
		if N == 0:
			ans += 'INSOMNIA'
		else:
			i = 0
			while seem_numbers != numbers:
				i += 1
				for elem in return_list_elements(list(str(i*N))):
					seem_numbers.add(elem)
			ans += str(i*N)
		print (ans)