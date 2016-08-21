import math
import sys

def is_prime(n):
	if n == 1:
		return False, 1
	elif n < 4:
		return True, -1
	elif n & 1 == 0:
		return False, 2
	elif n < 9:
		return True,-1
	elif n %3 == 0:
		return False, 3
	else:
		r = math.floor(math.sqrt(n))
		f = 5
		while f <= r:
			if n % f == 0:
				return False, f
			if n %(f+2) == 0:
				return False, f+2
			f += 6
		return True,-1

# def primeBelowM(m):
# 	num = [True for i in range(m)]
# 	for i in range(2,m):
# 		k = (m-1)/2
# 		for j in range(2,k+1):
# 			num[j*i] = False
# 	prime = []
# 	for i in range(2,m):
# 		if num[i]:
# 			prime.append(i)
# 	return prime

def convert_digits_2_num(digits, base):
    rslt=1 #last digits
    lenth=len(digits)+2
    rslt=rslt+pow(base,lenth-1)

    p=len(digits)-1
    for i in range(len(digits)):
        if digits[i]=="1":
            rslt=rslt+pow(base, p+1)
        p=p-1
    #print digits, base, rslt,####################################################
    return rslt


def validate(digits):
    #need to add 1 at head and tail of digits
    dividors=[]
    for i in range(2,11):
        num=long(convert_digits_2_num(digits,i))
        #print digits,i, num, ###################################################################3
        flag,div=is_prime(num)
        if flag==True:
            return False,[]
        else:
            dividors.append(div)

    return True, dividors

def output(digits, dividors):
    #output result
    lenth=len(digits)
    sdigt="1"
    for i in range(lenth):
        sdigt=sdigt+digits[i]
    print sdigt+"1",
    for i in range(9):
        print dividors[i],
    print

def solve(lenth,num):
    digits=[]
    cnt=0

    for i in range(int(lenth-2)):
        digits.append("0")

    brslt, dividors=validate(digits)
    if brslt==True:
        output(digits, dividors)
        cnt=cnt+1
        if cnt==num:
            return

    iend=lenth-2-1
    j=lenth-2-1

    while j>=0:
        if digits[j]=="0":
            digits[j]="1"
        else:
            while j>=0 and digits[j]=="1":
                j=j-1
            if j<0:
                break##########################################
            digits[j]='1'
            for k in range(j+1,iend+1):
                digits[k]='0'
            j=iend

        brslt, dividors=validate(digits)
        if brslt==True:
            output(digits, dividors)
            cnt=cnt+1
            if cnt==num:
                break


f_input=open(sys.argv[1])
#f_input=open("test.txt")
testcases=int(f_input.readline().rstrip())
for caseNr in xrange(1, testcases+1):
    line=f_input.readline().rstrip()
    fields=line.split()
    print("Case #%s:" % (caseNr))
    solve(int(fields[0]),int(fields[1]))
    #print("Case #%s: %s" % (caseNr, solve(num1,num2)))
f_input.close()