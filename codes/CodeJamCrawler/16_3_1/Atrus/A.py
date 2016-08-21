import string
import math
import codejamhelpers

# Solve here
def solve(S):
    solution = ""
    total = 0
    for p in S:
        total += p

    solution = evac(total, S)
    new_sol = ""
    for c in solution:
        if c is " ":
            new_sol += c
        else:
            new_sol +=string.ascii_uppercase[int(c)]
    return new_sol


def evac(total, S):
    sen = ""
    f_max = 0
    s_max = 0
    first = 0
    sec = 0
    for i, val in enumerate(S):
        if val >= f_max:
            s_max = f_max
            sec = first
            f_max = val
            first = i

    if f_max > total / 2:
        return "bad"
    if f_max == 0:
        return ""
    two = list(S)
    two[first] -=1
    if s_max == f_max:
        two[sec] -=1
        sen = str(first) + str(sec)
    else:
        two[first] -=1
        sen = str(first) + str(first)

    strat = evac(total-2, two)
    if strat != "bad":
        return sen+ " " +strat

    sen = str(first)
    S[first] -= 1
    strat = evac(total-1, S)
    if strat != "bad":
        return sen + " " + strat
    return strat








if __name__ == "__main__":
    testcases = eval(input())
    for case_num in range(1, testcases+1):
        N = input()
        S = str(input()).split(" ")
        S = list(map(int, S))
        #new_S = list(zip(string.ascii_uppercase, S))
        print("Case #%i: %s" % (case_num, solve(S)))


def format_list_of_nums(l):
    """Returns a space separated list of numbers as a string"""
    if(l[0] != str(l[0])):
        l = map(str, l)
    final = " ".join(new_str)
    return final

def format_list_of_chars():
    """Returns a string with the chars concatenated"""
    final = "".join(new_str)
    return final
