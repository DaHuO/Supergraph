#!/usr/bin/env python
import sys, os.path 

PROBLEM_ID = "A" # A B or C
PROBLEM_SIZE = "small"


def isBestFriendCircle( friendcircle, bestfriend_dict ):
    isCircle = True
    cnt = len(friendcircle)
    
    for i in range(cnt):
        if bestfriend_dict[i] != friendcircle[(i+1) % cnt] and \
            bestfriend_dict[i] != friendcircle[(i-1) % cnt]:
            isCircle = False
            break
        
    return isCircle


file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
in_f = open('{}.in'.format(file_name), 'r')
rl = in_f.readline

testcases = rl()
n = 1


printFlag = False

        
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
assert(len(alphabet) == 27)

while n <= int(testcases):
    nr_of_parties = int(rl().rstrip())
    pi = [ int(arg) for arg in rl().rstrip().split(" ")]
    
    plan = ""
    while sum(pi) > 0 :
        c2 = -1
        majority = sum(pi) // 2 + 1
        for i in range(nr_of_parties):
            if pi[i] == max(pi):
                c1 = i
                pi[i] -= 1
                break
        # one more senator to evacuate?
        majority = sum(pi) // 2
        for i in range(nr_of_parties):
            if pi[i] == max(pi):
                c2 = i
                pi[i] -= 1
                if sum(pi) // 2 + 1 <= max(pi):
                    pi[i] += 1
                    c2 = -1
                break
        plan += alphabet[c1] + alphabet[c2] + " "
        if sum(pi) // 2  + 1 <= max(pi):
            print sum(pi)
            print max(pi)
            print plan
            print pi
            quit()
        if printFlag:
            print nr_of_parties 
            print pi
        
        
    answer = str(plan.rstrip() )
    
    print "Case #" + str(n) + ": " + answer
    n = n + 1



