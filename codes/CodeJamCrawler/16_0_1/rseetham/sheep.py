import sys

def sheep(n) :
 	sleep = 0b0000000000
 	if n == 0 :
 		return "INSOMNIA"
 	i = 0
 	while True :
 		N = n * (i + 1)
 		last = N
 		i = i + 1
 		while N != 0 :
 			digit = int(N % 10)
 			val = 1 << digit
 			if val & sleep == 0 :
 				sleep = sleep | val
 				if sleep == 0b1111111111 :
 					return str(last) 
 			N = int(N / 10)

if __name__ == '__main__':
	try :
		t = int(input())
		for i in range(1, t + 1):
			n = int(input())
			print("Case #%i: %s" % (i, sheep(n)))
	except EOFError:
		print ("Error: EOF or empty input!")
