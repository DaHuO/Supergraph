def calculateNumber(numb):
    arr = [0,0,0,0,0,0,0,0,0,0]
    #print arr
    count=0;
    number = numb
    check = sum(arr)
    while(sum(arr)!=10):
        number_string = str(number)
        #print number_string
        for ch in number_string:
            arr[int(ch)] = arr[int(ch)] or 1
            #print arr
        count = count+1
        number = count*numb
        if(count==1000000):
        	return 'INSOMNIA'
    return numb*(count-1)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
#print t
for i in xrange(1, t + 1):
  n = int(raw_input())  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, calculateNumber(n))
  # check out .format's specification for more formatting options
  