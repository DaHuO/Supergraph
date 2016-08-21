'''
Created on 09.04.2016

@author: uscheller
'''
import sys


def flip(S, i):
    to_flip = S[0:i][::-1]
    flipped = to_flip.replace("+", ".").replace("-", "+").replace(".", "-")
    return flipped + S[i:]

def possible_flips(S):
    flips = []
    for i in range(1, len(S) + 1):
        flips.append(flip(S, i))
    return flips

def solve(S):
    queue = [(0, S)]
    checked_before = set()
    while True:
        flips, S = queue.pop(0)
        if S == "+" * len(S):
            return flips
        for new_S in possible_flips(S):
            if not new_S in checked_before:
                queue.append((flips + 1, new_S))
                checked_before.add(new_S)
            

def go_through(data):
    data = data[1:]
    s = ""
    case = 1
    while len(data) > 0:
        S = data[0].replace("\n", "")
        data = data[1:]
        s += "Case #%d: %s\n" % (case, solve(S))
        case += 1
    return s[:-1] # remove newline

if __name__ == '__main__':
    print go_through(open(sys.argv[1]).readlines())
    
    
    
    