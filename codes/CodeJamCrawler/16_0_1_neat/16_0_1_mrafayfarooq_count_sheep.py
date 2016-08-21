from sys import argv
def countSheep(n):
    digits = [None]*10;
    j=1;
    N=n;
    terminator=100
    while None in digits and terminator>0:
        n_string = str(N)
        for i in n_string:
            if(digits[int(i)]!=i):
                digits[int(i)]=i;
        j+=1;
        N=n*j
        terminator-=1;
    return (n*(j-1)) if terminator>0 else "INSOMNIA"
# target = open('A-large.out', 'w')
# with open('A-large.in', 'r') as f:
#     t = f.readline();
#     for line in range(1,int(t)+1,1):
#       num = int(f.readline())
#       print "Case #%d: %s" % (line, countSheep(num))
#       target.write("Case #%d: %s\n" % (line, countSheep(num)))
#for console
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())  # read a list of integers, 2 in this case
  print "Case #%d: %s" % (i, countSheep(n))
  # check out .format's specification for more formatting options
