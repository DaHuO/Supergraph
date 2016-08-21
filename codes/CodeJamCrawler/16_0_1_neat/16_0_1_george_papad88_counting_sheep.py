#!/usr/bin/python


def solve(num,step,digits):
	if len(digits)==10:
		return num
	else:
		num+=step
		return solve(num,step,digits|getDigits(num))

def getDigits(num):
	digits=set()
	for ch in str(num):
		digits.add(ch)
	return digits

def main():
	with open('large.txt') as input:
        	number_of_rows = input.readline()        #discard line
        	number=input.readline()
	        cnt=1
	        while number:
			num=int(number)
			res = "INSOMNIA"
			if num <> 0:
	        	        res = solve(num,num,getDigits(num))
        	        print ('Case #%d: %s' % (cnt,str(res)))
                	cnt+=1
        	        number=input.readline()


if __name__ == "__main__":
    main()
