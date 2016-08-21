# tcases=int(input())
# case=1
# def maneovre(stack):
# 	# flipping implies REVERSE COMPLEMENTATION of the i pies in consideration
# 	# if there is + on top of stack, flip TILL FIRST(EXCLUDING that -) - encountered(unless all +)
# 	# else get the last -, flip stack INCLUDING that minus
# 	# recursive


# 	#analytical method:
# 	#find number of -+ and +-
# 	# every -+ contributes to 1 step(but must appear before any occurences of +-)
# 	# every +- contributes to 2 steps
# 	def find_offsets(stack, n):
# 		offs = -1
# 		while True:
# 			offs = stack.find(n, offs+1)
# 			if offs == -1:
# 				break
# 			else:
# 				yield offs

# 	# print(list(find_offsets("--+-+-", "+-")))
# 	# print(list(find_offsets("--+-+-", "-+")))
# 	if set(stack)=={'+'}:return 0
# 	if set(stack)=={'-'}:return 1
# 	a=list(find_offsets(stack, "+-"))
# 	m=min(a.__add__([len(stack)]))
# 	b=list(filter(lambda x:x<m,list(find_offsets(stack, "-+"))))
# 	# print(a)
# 	# print(b)
# 	return (len(a)*2)+len(b)
# while case<=tcases:
# 	print('Case #'+str(case)+':',end=' ')
# 	stack=input()
# 	print(maneovre(stack))
# 	case+=1

tcases=int(input())
case=1
def maneovre(stack):
	def find_offsets(stack,boundary_pancake):
		ind=-1
		while True:
			ind = stack.find(boundary_pancake,ind+1)
			if ind==-1:break
			else:yield ind

	if set(stack)=={'+'}:return 0
	if set(stack)=={'-'}:return 1
	a=list(find_offsets(stack, "+-"))
	m=min(a.__add__([len(stack)]))
	b=list(filter(lambda x:x<m,list(find_offsets(stack, "-+"))))
	return (len(a)*2)+len(b)

while case<=tcases:
	print('Case #'+str(case)+':',end=' ')
	stack=input()
	print(maneovre(stack))
	case+=1