def main():
	for t in range(int(input())):
		digits = [0] * 10
		n = int(input())
		check = 1
		res = "INSOMNIA"
		for i in range(1, 10001):
			m = str(n * i)
			for x in m:
				digits[int(x)] = 1
			check = 1		
			for i in range(10):
				if digits[i] == 0:
					check = 0
					break
			if check == 1:
				res = m 
				break
			
		print("Case #"+ str(t + 1) +": " +res)

if __name__ == '__main__':
	main()