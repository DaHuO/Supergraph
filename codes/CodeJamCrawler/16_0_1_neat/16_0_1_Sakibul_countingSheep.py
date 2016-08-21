def sheep(n):
  # check out .format's specification for more formatting optionsdef sheep(n):
    increase=n
    digitslist=[]
    print('hey'+str(n))
    if n==0:
        return 'INSOMNIA'
    else:
        while len(digitslist)<10:
            for digit in str(n):
                #Check to see if we have seen the digit
                if int(digit) not in digitslist:
                    digitslist.append(int(digit))
                #Check to see if we have seen all the digits. If so, return n
            if len(digitslist)==10:
                return n
            else:
                n=n+increase

inputfile = open('A-large.in', 'r')
outputfile=open("output.txt",'w')
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(inputfile.readline())  # read a line with a single integer, the test case
  # check out .format's specification for more formatting optionsdef sheep(n):
for i in xrange(1, t + 1):
    n=inputfile.readline().strip('\n')
    print(n)
    print "Case #"+str(i)+": "+str(sheep(int(n)))
    outputfile.write("Case #"+str(i)+": "+str(sheep(int(n)))+"\n")