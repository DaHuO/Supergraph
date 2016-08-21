__author__ = 'pranavgupta'
from collections import defaultdict
import re
import copy

def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:]
    return mystring

list_num = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
dict_num = {list_num[i]:i for i in range(len(list_num))}
global answer
global req

def find_num(S):
    flag = 1
    for word in list_num:
        global answer
        if len(S) == 0:
            return answer
        oldS = S
        flag = 1
        for tchar in word:
            if tchar in S:
                S = S.replace(tchar,'',1)
            else:
                S = oldS
                flag = 0
                break
        if flag:
            # print word
            # print dict_num[word]
            # print S
            answer.append(str(dict_num[word]))
            # print answer
            # print S
            if len(S) == 0:
                global req
                req = copy.deepcopy(answer)
                return True
            else:
                if(find_num(S)):
                    return True
                S += word
                answer.remove(str(dict_num[word]))


if __name__ == '__main__':
    T = long(raw_input())
    for i in range(T):
        S = raw_input()
        global answer
        answer = []
        global req
        req = []
        find_num(S)
        print "Case #{0}: {1}".format(i+1,"".join(sorted(req)))