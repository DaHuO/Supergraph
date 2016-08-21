# revenge of the Pancakes
# suhas kashyap
# kashyap 07
# kashyapsuhas07@gmail.com

def find_flips(N):
	turns = 0
	for i in range(len(N) - 1):
		turns += N[i] != N[i+1]
	if(N[-1]) ==  "-":
		turns = turns + 1
	return what_to_print(turns)

def what_to_print(turns):
	print("Case #", i+1, ": ", turns, sep = '')

if __name__ == "__main__":
	T = int(input())	# T test cases
	N = [] *T 			# N Number
	for i in range(T):
		N.append(input())
	for i in range(T):
		find_flips(N[i])