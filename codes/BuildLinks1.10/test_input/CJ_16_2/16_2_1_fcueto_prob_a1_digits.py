"""
Fernando Gonzalez del Cueto
Google Code Jam Round 2

Problem A
"""

from codejam import Problem
import copy
from collections import Counter
import numpy as np
import pandas as pd
import scipy.optimize as sciopt


# input_file = 'test.in'
input_file = 'A-small-attempt0.in'
prob = Problem(input_file)

# digits = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
digits = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"}
s = list(set(''.join(["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN","EIGHT", "NINE"])))
s.sort()

n_letters = len(s)
template = pd.DataFrame(index=range(10), columns=s, data=0, dtype=float)

dic = template.copy()
for dig in range(10):
    for letter in digits[dig]:

        dic.loc[dig,letter] +=1


n_cases = prob.parse_int()
for case_j in range(1, n_cases+1):

    #fid_in = prob.f_in

    stream = prob.readline().strip()
    c = Counter(stream)
    t1 = pd.Series(c, index=s).fillna(0)

    A = dic.values.T
    c = np.ones((10,))
    result = sciopt.linprog(c=c, A_eq=A, b_eq=t1.values )

    result['x']

    sol = result['x'].astype(np.uint32)

    number = ''
    for i in range(10):
        if sol[i]>0:
            number += str(i)*sol[i]

    # print(case_j, l)

    out_line = number
    prob.write(case_j, out_line, print_out=True)

# close input and output files
prob.close()