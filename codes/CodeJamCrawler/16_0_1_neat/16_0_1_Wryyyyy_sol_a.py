#!/usr/bin/env python

def counting_sheep(x):
        S= set()
        L= []
        a= x
        while True:
            C= list(str(a))
            for c in C:
                S.add(c)
                if len(S)==10:
                    return str(a)
            if a in L:
                break
            L.append(a)
            a+=x
	return 'INSOMNIA' 

def main():
            
	T= int(raw_input())
	for i in range(1,T+1):
		N= int(raw_input())
		print "Case #%d: %s"%( i, counting_sheep(N) );		

if __name__ == '__main__':
	main()

