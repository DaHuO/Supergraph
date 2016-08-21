import sys
import pyprimes
import pyprimes.factors

path_input=sys.argv[1]
path_output = sys.argv[2]
#print path_input
#print path_output


_input = open(path_input,"r")
_output = open(path_output,"w")


t = int(_input.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, J = [int(s) for s in _input.readline().split(" ")]  # read a list of integers, 2 in this case
    print N," et ", J
    assert(N>=2)
    current = "1"+"0"*(N-2)+"1"
    number_of_found = 0

    _output.write("Case #{}:\n".format(i))
    divisors=[]
    while (number_of_found<J):
        for base in range(2,11):
            number_in_base = int(current,base)
            print current
            if pyprimes.is_prime(number_in_base):
                current = str(bin(int(current,2)+2))[2:]
                divisors = []
                break
            else:
                divisors.append(list(pyprimes.factors.factors(number_in_base))[0][0])
        assert(len(divisors)==9 or  len(divisors)==0)
        if(len(divisors)==9):
            number_of_found+=1
            print_divisors = ' '.join([str(k) for k in divisors])
            _output.write(current+" "+print_divisors+'\n')
            current = str(bin(int(current,2)+2))[2:]
            divisors =[]


_output.close()
_input.close()

