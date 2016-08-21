#!/usr/bin/env python
import re
Q= [ 
   ( 1, re.compile('^[\-]+[\+]+'), '+' ),
   ( 2, re.compile('^[\+]+[\-]+'), '+' ),
   ( 1, re.compile('^[\-]+$')    , '' ),
   ( 0, re.compile('^[\+]+$')    , '' ),
]
def revenge(S):
        r= 0
        while len(S):
            for f,t,prefix in Q:
                y= t.findall(S)
                if y:
                    S= prefix + S[len(y.pop()):]
                    r+= f
                    break
	return r

def main():
            
	T= int(raw_input())
	for i in range(1,T+1):
		S= (raw_input()).strip()
		print "Case #{}: {}".format( i, revenge(S) );		

if __name__ == '__main__':
	main()

