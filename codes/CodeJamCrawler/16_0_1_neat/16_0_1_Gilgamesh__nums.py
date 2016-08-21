import sys

def test(n):
   	tracker = {}
	n = int(n)
  	if n == 0:
 		return 'INSOMNIA'
        i = 1
	while True:
        	curr = (i*n)
                for number in str(curr):
                	tracker[number] = 1 
        	sum = 0
                for item in tracker:
                	sum += tracker[number]
   		if sum == 10:
           		return curr
 		i += 1
 

if __name__=="__main__":
	with open('A-large.in', 'r') as f:
		total_number = f.next()
		i = 1
		for line in f:
			print 'Case #'+str(i)+': '+str(test(line))
			i += 1
