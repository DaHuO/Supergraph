#This file is for Problem 2 in the Qualification Round Google Code Jam 2016
#Written by Chuqiao Ren
#All rights reserved

def reverseString(s):
    l = len(s)
    result = ''
    for i in range(len(s)):
        if s[l - 1 - i] == '+':
            result += '-'
        else:
            result += '+'

    return result

def findFirstBlack(s):
    for i in xrange(len(s)):
        if s[len(s) - 1 - i] == '-':
            return len(s) - 1 - i

    return -1

def testSymmetric(s):
    if reverseString(s) == s:
        return True
    else:
        return False

def findFirstBlackSymmetric(s):
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            return i
    return

def process(s):
    count = 0
    if s[-1] == '-':
        count = 1
    for i in range(1,len(s)):
        index = len(s) - 1 - i
        if s[index] != s[index +1]:
            count += 1
    return count

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = [s for s in raw_input().split(" ")][0] # read a list of integers, 1 in this case
  result = process(n)
  print "Case #{}: {}".format(i, result)
# print findFirstBlack("+-")
# print findFirstBlackSymmetric("+-")
# print testSymmetric("+-")