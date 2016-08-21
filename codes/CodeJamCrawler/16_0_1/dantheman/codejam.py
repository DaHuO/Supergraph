#! /usr/bin/pyyhon

import sys

fh = open('sample.txt', 'r')
ipArray = fh.read().split('\n')
n = ipArray[0]
ip = ipArray[1:-1]
maxi = set(['0','1','2','3','4','5','6','7','8','9'])

itr = 1
for i in ip:
    
    a = set([])
    p = 1
    prev = 0
    forever_flag = 0
    while(a != maxi):
	
 	x = int(i) * p
 	if(prev == x):
 	    forever_flag = 1
	    break
	else:
	    prev = x
  	p += 1
 	a = a | set(list(str(x)))
    if forever_flag == 1:
	print "Case #%s: INSOMNIA" % (itr)
    else:
     	print "Case #%s:" % (itr), x
    itr += 1
