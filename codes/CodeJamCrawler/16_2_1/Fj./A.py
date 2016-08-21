import pdb
import sys
import re
import time
import collections
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob

taskname = 'A'
input_file = None

def readstr():
    return next(input_file).strip()


def readintlist():
    lst = list(map(int, readstr().split()))
    return lst


def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]


WORDS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def uniquely_determined(words):
    set_unique = {}
    for word in words:
        rest = set(c for w2 in words if w2 != word for c in w2)
        unique = [c for c in word if c not in rest]
        if unique:
            set_unique[word] = unique
    return set_unique

def get_ud_tiers():
    words = set(WORDS)
    tiers = []
    while words:
        unique = uniquely_determined(words)
        assert unique, 'remaining: ' + str(words) 
        tiers.extend(list(unique.items()))
        words = set(words) - unique.keys()
    return tiers
    
tiers = get_ud_tiers()
      

def solvecase():
    s = readstr()
    counts = collections.Counter(s)
    result = {}
    for word, letters in tiers:
        l = letters[0]
        wordcounts = collections.Counter(word)
        cnt = counts[l] // wordcounts[l]
        if cnt:
#             print(word, cnt, counts)
            result[WORDS.index(word)] = cnt 
            counts.subtract({k : v * cnt for k, v in wordcounts.items()})
    assert not any(counts.values()), counts
    return ''.join(str(d) * cnt for d, cnt in sorted(result.items()))


def solve(input_name, output_name):
    global input_file
    tstart = time.clock()
    with open(input_name, 'r') as input_file, open(output_name, 'w') as output_file:
        casecount = readint()
        
        for case in range(1, casecount + 1):
            s = solvecase()
            s = "Case #%d: %s" % (case, str(s)) 
            print(s, file=output_file)
            print(s)
        
    print('%s solved in %.3f' % (input_name, time.clock() - tstart))


def main():
    input_names = glob(taskname + '-*.in')
    assert len(input_names)
    input_names.sort(reverse = True)
    for input_name in input_names:
        solve(input_name, input_name.replace('.in', '.out')) 
                

if __name__ == '__main__':
    main()
