def resolver(str):
	res = str[:1]
	for c in str[1:]:
		if res + c > c + res:
			res = res + c
		else:
			res = c + res
	return res

def main():
	T = int(input().strip())
	for i in range(1, T+1):
		print("Case #{}: {}".format(i, resolver(input().strip())))

main()
