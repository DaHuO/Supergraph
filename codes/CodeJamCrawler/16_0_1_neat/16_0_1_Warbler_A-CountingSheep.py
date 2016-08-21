#!/usr/bin/env python
# -*- coding: utf-8 -*-


add0_reminder={}
add0_flag={}
add1_reminder={}
add1_flag={}

def preprocess():
    global add0_reminder,add0_flag,add1_reminder,add1_flag
    for i in range(10):
        for j in range(10):
            si=str(i)
            sj=str(j)
            if add0_reminder.has_key(si)==False:
                add0_reminder[si]={}
                add0_flag[si]={}
                add1_reminder[si]={}
                add1_flag[si]={}

            add0_reminder[si][sj]=str((i+j)%10)
            add0_flag[si][sj]=str((i+j)/10)

            add1_reminder[si][sj]=str((i+j+1)%10)
            add1_flag[si][sj]=str((i+j+1)/10)

def add(rslt, num, digits):
    global add0_reminder,add0_flag,add1_reminder,add1_flag
    new_rslt=""

    i=len(rslt)-1
    j=len(num)-1

    flag="0"
    remind=""
    while i>=0 and j>=0:
        si=rslt[i]
        sj=num[j]
        if flag=="0":
            remind=add0_reminder[si][sj]
            flag=add0_flag[si][sj]
        else:
            remind=add1_reminder[si][sj]
            flag=add1_flag[si][sj]
        digits[remind]=1
        new_rslt=remind+new_rslt
        i=i-1
        j=j-1

    if i<j:
        while j>=0:
            sj=num[j]
            remind=add0_reminder[flag][sj]
            flag=add0_flag[flag][sj]
            new_rslt=remind+new_rslt
            digits[remind]=1
            j=j-1
    elif i>j:
        while i>=0:
            si=rslt[i]
            remind=add0_reminder[si][flag]
            flag=add0_flag[si][flag]
            new_rslt=remind+new_rslt
            digits[remind]=1
            i=i-1

    if flag!="0":
        new_rslt=flag+new_rslt
        digits["1"]=1

    return new_rslt

def solve(num):
    if num=="0":
        return "INSOMNIA"

    digits={}
    rslt="0"
    while True:
        rslt=add(rslt, num, digits)
        if len(digits)==10:
            return rslt


#if __name__ == "__main__":
preprocess()
testcases = input()
for caseNr in xrange(1, testcases+1):
    num = raw_input()
    print("Case #%s: %s" % (caseNr, solve(num)))

