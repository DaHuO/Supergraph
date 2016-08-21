import itertools


dic = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def write(out, case, answer):
	out.write("Case #%d: " %(case))
	out.write(str(answer) + "\n")

def parse(f):
	f = open(f, "r").read().split("\n")
	n = f[0]
	return n, f[1:]



def get_numbers(n):
	for i in range(n):
		i = str(i)
		yield i.zfill(len(str(n))-1)

def test_single_number(n):
	concat = ""
	for i in n:
		concat += dic[int(i)]
	return sorted(concat)

def get(word):
	for i in range(10):
		iterator = get_numbers(10**i)
		while True:
			try:
				n = iterator.next()
				test = test_single_number(n)
				if sorted(word) == sorted(test):
					return n
			except StopIteration:
				break

def main():
	n, words = parse("A-small-attempt0.in")
	outfile = open("A-small-out.txt","w")
	n = int(n)
	for i in range(n):
		number = get(words[i])
		write(outfile, i+1, number)
	

main()
# print main("OZONETOWER")
# print main("WEIGHFOXTOURIST")
# print main("OURNEONFOE")
# print main("ETHER")


