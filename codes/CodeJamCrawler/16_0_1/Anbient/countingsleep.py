#!/usr/bin/env python
# -*- coding: utf-8 -*-

myGlobal = 0

def fall_asleep(array):
    for i in xrange(0, 10):
        if (array[i] == 0):
            return False
    return True

def countSleep(num_str, array, n):
    global myGlobal

    num = int(num_str)
    if (num == 0):
        myGlobal = "INSOMNIA"
        return

    number_string = str(num*n);

    #print("number_string: %s" % (number_string))

    for ch in number_string:
        array[int(ch)] = 1

    if (not fall_asleep(array)):
        countSleep(num, array, n+1)
    else:
        myGlobal = n * num



if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		countSleep(cipher, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1)
		print("Case #%i: %s" % (caseNr, myGlobal))
