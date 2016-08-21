#!/usr/bin/python


def solve(lst):
	res=[lst[0]]
	previous = lst[0]
	for curr in lst:
		if curr <> previous:
			res.append(curr)
			previous=curr
#	print res
	return len(res) if previous == '-' else len(res)-1

def main():
	with open('large.txt') as input:
        	number_of_rows = input.readline()        #discard line
        	line=input.readline()
	        cnt=1
	        while line:
			line = line.strip()
        	        print ('Case #%d: %d' % (cnt,solve(line)))
                	cnt+=1
			line=input.readline()


if __name__ == "__main__":
    main()
