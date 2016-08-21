def seen(n, dic):
	for i in (str(n)):
		if i not in dic:
			dic[i] = -1

def main(n, dic):
	i = 1
	while (True):
		seen(n*i, dic)
		if len(dic)==10:
			break
		i += 1
	return n*i

def read():
	f = open("A.txt", "r").read().split()
	out = open("Aout.txt", "w")
	total = f[0]
	case = 1
	for n in f[1:]:
		out.write("Case #%d: " %(case))
		if int(n) == 0:
			out.write("INSOMNIA\n")
		else:
			dic = {}
			if case==100:
				out.write("%d" %(main(int(n),dic)))
			else:
				out.write("%d\n" %(main(int(n),dic)))
		case += 1


read()
# seen(5)
# print dic