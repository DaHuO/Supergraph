def solve(N):
	if N == 0:
		return 'INSOMNIA'
	else:
		digits_seen = {}
		mult = 1
		while len(digits_seen) < 10:
			num = str(mult*N)
			print num
			for i in range(len(num)):
				digits_seen[num[i]] = 1
			mult += 1	
	return num

def print_solution(ans):
  f = open('output_small.txt', 'w')
  for i in range(len(ans)):
    f.write("Case #" + str(i+1) + ": " + str(ans[i]) +"\n")

if __name__ == '__main__':
  #test()
  f = open('A-large.in')
  T = int(f.readline())
  answers = [0]*T
  for i in range(T):
    N = f.readline()      
    answers[i] = solve(int(N))    
    print answers[i]
  print answers
  print_solution(answers)

	