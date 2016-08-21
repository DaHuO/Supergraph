def fact(n):
	if n == 0:
		return 1
	res = n
	n -= 1
	while n > 0:
		res *= n
		n -= 1
	return res

def number_of_seq(n):
	result = 0
	for i in range(n+1):
		if i == 0:
			result += 1
		else:
			result += fact(n)//fact(n-i)
	return result
			
			
def quantity(now, board, was, B):
	was = list(was)
	was.append(now)
	if now == B-1:
		return 1
	else:
		res = 0
		for i in range(B):
			if board[now][i] == 1 and i not in was:
				res += quantity(i, board, was, B)
		return res
	
def generate_board(board, i, B, boards):
	jey = i // B
	ind = i % B
	if jey == B - 1:
		boards.append(board)
	
	elif board[jey][ind] == 1:
		copy_board = [list(i) for i in board] 
		copy_board[jey][ind] = 0
		generate_board(copy_board, i+1, B, boards)
		
		copy_board = [list(i) for i in board]
		generate_board(copy_board, i+1, B, boards)
	else:
		copy_board = [list(i) for i in board]
		generate_board(copy_board, i+1, B, boards)
		
		
	

with open("B-small-attempt1.in", "r") as f:
	t = int(f.readline())


	result = ""

	for i in range(t):
		line = f.readline()
		B = int(line.split()[0])
		M = int(line.split()[1])
		result += "Case #" + str(i+1) + ":"
		
		maxM = number_of_seq(B-2)
		if maxM < M:
			result += " IMPOSSIBLE"
		else:
			
			full_board = [[0 for i in range(B)] for i in range(B)]
			for i in range(B-1):
				for j in range(i+1,B):
					full_board[i][j] = 1
			print(full_board)
			
			boards = []
			
			generate_board(full_board, 0, B, boards)
			res = False
			for board in boards:
				if quantity(0, board, [], B) == M:
					res = board
					break
			print(res)
			print(quantity(0, board, [], B))
			if res:
				result += " POSSIBLE"
				for line in res:
					result += "\n"
					for letter in line:
						result += str(letter)
			else:
				result += " IMPOSSIBLE"
				
			
			
		result += '\n'
		
	
with open("output.txt", "w") as f:
	f.write(result)
