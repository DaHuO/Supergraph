
def problemB():
	stack = []
	stack_str = raw_input()
	for c in stack_str:
		stack.append(c)

	stack = list(reversed(stack))
	mov = 0
	while not all_positive(stack):
		stack, stack_aux = fill_stack_aux(stack)
		stack_aux = flip_flip(stack_aux)
		mov = mov + 1
		stack = stack + stack_aux
	return mov

def flip_flip(stack_aux):
	stack_aux = list(reversed(stack_aux))
	for inx in range(len(stack_aux)):
		if stack_aux[inx] == '-':
			stack_aux[inx] = '+'
		else:
			stack_aux[inx] = '-'
	return stack_aux

def fill_stack_aux(stack):
	only_neg = False
	stack_aux = []

	while not stack_is_enpty(stack):	
		elem = stack.pop()
		if elem == '+' and only_neg:
			stack.append(elem)
			return stack, stack_aux
		else: 
			if elem == '-':
				only_neg = True
			stack_aux.append(elem)

	return stack, stack_aux

def stack_is_enpty(stack):
	if not stack:
		return True
	return False

def all_positive(stack):
	for elem in stack:
		if elem == '-':
			return False
	return True

if __name__ == '__main__':
	T = int(raw_input())
	case = 1
	while T>0:
		print "Case #%s: %s" % (case, problemB())
		case = case + 1
		T = T - 1