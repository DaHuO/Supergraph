def selection_sort(lst):
	
	for i in range(0,len(lst)):
		for g in range(1,len(lst)): 
			if lst[g] < lst[g-1]:
				lst[g-1], lst[g] = lst[g], lst[g-1]
	return lst
				
def main():
		
		N = int(input())
		
		
		for q in range(N):
			
			S = input()
			
			num_z = 0
			num_w = 0
			num_x = 0
			num_u = 0
			num_g = 0
			num_f = 0
			num_t = 0
			num_v = 0
			num_o = 0
			num_i = 0
			
			answer_list = []
			char_list = list(S)
			
			selection_sort(char_list)
			
			for i in range(len(char_list)):
				
				if char_list[i] == 'Z':
					num_z += 1
					
				elif char_list[i] == 'W':
					num_w += 1
				
				elif char_list[i] == 'X':
					num_x += 1
					
				elif char_list[i] == 'U':
					num_u += 1
					
				elif char_list[i] == 'G':
					num_g += 1
	
			
			for i in range(num_z):
				answer_list.append('0')
				char_list.remove('Z')
				char_list.remove('E')
				char_list.remove('R')
				char_list.remove('O')
				
			for i in range(num_w):
				answer_list.append('2')	
				char_list.remove('T')
				char_list.remove('W')
				char_list.remove('O')

			for i in range(num_x):
				answer_list.append('6')
				char_list.remove('S')
				char_list.remove('I')
				char_list.remove('X')

			for i in range(num_u):
				answer_list.append('4')
				char_list.remove('F')
				char_list.remove('O')
				char_list.remove('U')
				char_list.remove('R')
				
			for i in range(num_g):
				answer_list.append('8')
				char_list.remove('E')
				char_list.remove('I')
				char_list.remove('G')
				char_list.remove('H')
				char_list.remove('T')
				
			for x in range(len(char_list)):
				
				if char_list[x] == 'F':
					num_f += 1
					
				elif char_list[x] == 'T':
					num_t += 1
					
			for i in range(num_f):
				answer_list.append('5')
				char_list.remove('F')
				char_list.remove('I')
				char_list.remove('V')
				char_list.remove('E')
				
			for i in range(num_t):
				answer_list.append('3')
				char_list.remove('T')
				char_list.remove('H')
				char_list.remove('R')
				char_list.remove('E')
				char_list.remove('E')
				
			
			for y in range(len(char_list)):
				
				if char_list[y] == 'V':
					num_v += 1
					
				elif char_list[y] == 'O':
					num_o += 1
					
				elif char_list[y] == 'I':
					num_i += 1
					
			for i in range(num_v):
				answer_list.append('7')
				char_list.remove('S')
				char_list.remove('E')
				char_list.remove('V')
				char_list.remove('E')
				char_list.remove('N')
				
			for i in range(num_o):
				answer_list.append('1')
				char_list.remove('O')
				char_list.remove('N')
				char_list.remove('E')
				
			for i in range(num_i):
				answer_list.append('9')
				char_list.remove('N')
				char_list.remove('I')
				char_list.remove('N')
				char_list.remove('E')

			answer_lst = selection_sort(answer_list)
			
			answer = "".join(answer_list)
			
			
			print("Case #", q+1 , ": ", answer,  sep = "")

					
main()
	
	

			