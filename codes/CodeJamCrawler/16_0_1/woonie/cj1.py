def check(num, cur, mul):
    numnum = num*mul
    while numnum > 0:
        i = numnum%10
        
        if i in cur:
            cur.remove(i)
        numnum /= 10
    if len(cur) > 0:
    	return check(num, cur, mul+1)
    else:
    	return num * mul
def main():
	
	f = open('cj1large.txt', 'r')
	l = int(f.readline())
	for i in range(l):
		a = [0,1,2,3,4,5,6,7,8,9]
		out = "Case #" + str(i+1) + ": "
		t = int(f.readline())
		if t == 0:
			out += "INSOMNIA"
		else:
			res = check(t, a, 1)
			

			out += str(res)
		print out

	
main()

