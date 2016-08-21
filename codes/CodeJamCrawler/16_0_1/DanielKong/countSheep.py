import sys
import pdb

# array = [False] * 10
StopCount = 0

def splitResult(newResult, array):
	while newResult > 0 :
		digit = int(newResult % 10)
		updateArray(digit, array)
		newResult /= 10
	
def updateArray(digit, array):
	if not array[digit]:
		array[digit] = True
		global StopCount
		StopCount = StopCount + 1

def main(argv):
    # My code here
    input = open("/Users/daniel.kong/Downloads/A-large.in", "r")
    result = open('/Users/daniel.kong/Documents/codeJam_Python/test-large.txt', 'w')
    count = int(input.readline())
    print count
    for j in range(count):
    	N = int(input.readline())
    	#print N
    	#pdb.set_trace()
    	i = 0
    	if N == 0:
    		result.write('Case #%d: INSOMNIA\n' % int(j+1))
    		continue
    	else:
    		array = [False] * 10
    		global StopCount
    		StopCount = 0
    		while StopCount < 10:
    			i = i +  1
    			temp = int(N * i)
    			splitResult(temp, array)
    	result.write('Case #%d: %d\n' %  (j+1, N * i))

if __name__ == "__main__":
    #N = input("Enter a number: ")
    main(sys.argv)
