import sys
from sets import Set
from collections import Counter
import math
from math import *

path_input=sys.argv[1]
path_output = sys.argv[2]
#print path_input
#print path_output


_input = open(path_input,"r")
_output = open(path_output,"w")

def check_and_remove(St,number,digit,letter_,spelled):
    while letter_ in St:
        for letter in list(spelled):
            St.remove(letter)
        number.append(digit)
    return St,number


t = int(_input.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    S = list(_input.readline().rstrip())
    print S
    number = []
    S,number = check_and_remove(S,number,0,'Z',"ZERO")
    S,number = check_and_remove(S,number,2,'W',"TWO")
    S,number = check_and_remove(S,number,6,'X',"SIX")
    S,number = check_and_remove(S,number,8,'G',"EIGHT")
    S,number = check_and_remove(S,number,7,'S',"SEVEN")
    S,number = check_and_remove(S,number,5,'V',"FIVE")
    S,number = check_and_remove(S,number,4,'F',"FOUR")
    S,number = check_and_remove(S,number,3,'H',"THREE")
    S,number = check_and_remove(S,number,1,'O',"ONE")
    S,number = check_and_remove(S,number,9,'N',"NINE")
    
    print S
    assert(len(S)==0)
    number=sorted(number)
    _output.write("Case #{}: {}\n".format(i,''.join([str(k) for k in number])))

_output.close()
_input.close()

