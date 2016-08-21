import sys

def flip_pancakes(stack):
	if stack == '+':
		return 0
	elif stack == '-':
		return 1
		
	if stack[0] != stack[1]:
		return 1 + flip_pancakes(stack[1:])
	else:
		return flip_pancakes(stack[1:])

def main():
	T = int(sys.stdin.readline().strip())
	
	for i in range(T):
		stack = sys.stdin.readline().strip()
		print("Case #{0}: {1}".format(i+1, flip_pancakes(stack)))
		
if __name__ == '__main__':
	main()