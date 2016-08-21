import sys
from collections import Counter


digs_dict = {"ZERO":0,
"ONE":1,
"TWO":2,
"THREE":3,
"FOUR":4,
"FIVE":5,
"SIX":6,
"SEVEN":7,
"EIGHT":8,
"NINE":9}

digs_dict_back = {0:"ZERO",
1:"ONE",
2:"TWO",
3:"THREE",
4:"FOUR",
5:"FIVE",
6:"SIX",
7:"SEVEN",
8:"EIGHT",
9:"NINE"}


digs_signatures = dict( (dig,dict(Counter(sig))) for dig,sig in digs_dict_back.iteritems() )

def subtract_digs(big_str_signature,digit,times):
    """subtract 'times' number of a digit signatures from the big string signature,
    assuming everything is correct ..."""
    for  let,count in digs_signatures[digit].iteritems():
        big_str_signature[let] -= count*times
    # return big_str_signature
    # WORKS FINE, CHANGING GLOBAL STATE, I.E. 'big_str_signature'
# xxx = {'S':4,'X':3,'I':3,'E':2,'V':1,'N':1}
# subtract_digs(xxx,6,3)


def Solve_Problem(big_string,verbose=False):
    extracted_digits = []
    big_str_signature = dict(Counter(big_string))
    if 'Z' in big_str_signature:
        times = big_str_signature['Z']
        subtract_digs(big_str_signature,0,times)
        extracted_digits += [0,]*times
    if 'W' in big_str_signature:
        times = big_str_signature['W']
        subtract_digs(big_str_signature,2,times)
        extracted_digits += [2,]*times
    if 'X' in big_str_signature:
        times = big_str_signature['X']
        subtract_digs(big_str_signature,6,times)
        extracted_digits += [6,]*times
    if 'S' in big_str_signature:
        times = big_str_signature['S']
        if times > 0:
            subtract_digs(big_str_signature,7,times)
            extracted_digits += [7,]*times
    if 'V' in big_str_signature:
        times = big_str_signature['V']
        if times > 0:
            subtract_digs(big_str_signature,5,times)
            extracted_digits += [5,]*times
    if 'F' in big_str_signature:
        times = big_str_signature['F']
        if times > 0:
            subtract_digs(big_str_signature,4,times)
            extracted_digits += [4,]*times
    if 'O' in big_str_signature:
        times = big_str_signature['O']
        if times > 0:
            subtract_digs(big_str_signature,1,times)
            extracted_digits += [1,]*times
    if 'G' in big_str_signature:
        times = big_str_signature['G']
        if times > 0:
            subtract_digs(big_str_signature,8,times)
            extracted_digits += [8,]*times
    if 'R' in big_str_signature:
        times = big_str_signature['R']
        if times > 0:
            subtract_digs(big_str_signature,3,times)
            extracted_digits += [3,]*times
    if 'I' in big_str_signature:
        times = big_str_signature['I']
        if times > 0:
            subtract_digs(big_str_signature,9,times)
            extracted_digits += [9,]*times
    ####################################
    assert sum(big_str_signature.values())==0
    return ''.join(map(str,sorted(extracted_digits)))


    

# IO business ..
problem_input = sys.stdin.readlines()
the_T = int(problem_input[0])
assert the_T == len(problem_input[1:])

for i,the_input in enumerate(problem_input[1:]):
    the_input = the_input.strip()
    print "Case #%d: %s"%(i+1,Solve_Problem(the_input))



















