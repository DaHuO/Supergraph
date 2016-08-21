happy = 0
unhappy = 1

def decode(input):
	result = list()
	return [happy if i == '+'  else unhappy for i in input]

def reverse_and_flip(stack):
	return [unhappy if i == happy else happy for i in reversed(stack)]
	
def lift_up(stack, position):
	to_lift = stack[:position]
	rest = stack[position:]
	return reverse_and_flip(to_lift) + rest
	
def encode(stack):
	result = ''
	for i in stack:
		if i == happy: result += '+'
		else: result += '-'
	return result
	
def backwards_method(stack):
	start = [happy] * len(stack)
	#print('stack', encode(stack))
	#print('start', encode(start))
	s = len(stack)
	steps = 0
	for i in range(s):
		j = s - i - 1
		if start[j] != stack[j]:
			start = lift_up(start, j + 1)
			#print('step', encode(start))
			steps += 1
	return steps
	
def solve(test):
	return str(backwards_method(decode(test)))

def run(solve):
	t = int(input())
	for i in range(1, t + 1):
	  print("Case #{}: {}".format(i, solve(input())))	

run(solve)