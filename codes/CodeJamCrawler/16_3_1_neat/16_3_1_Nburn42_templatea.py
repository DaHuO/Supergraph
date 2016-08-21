#!usr/bin/python2
import sys

def main():
	outputs = "Case #{}: {}"
	cases = int(raw_input())
	for case in xrange(cases):
                parties = int(raw_input())
		senns = map(int, raw_input().split())
                sta = ord('A')
                senas = map(chr, range(sta, sta+parties))
                sens = sorted(map(list, zip(senns, senas)))[::-1]
		#print sens
                output = []
                while sens[0][0] > 0:
                    ind = 0
                    while ind < parties and sens[ind][0] >= 0:
                        count = 0
                        exit = []
                        #print "e", ind, "c", count, "s", sens
                        while ind+count < parties and count < 2 and sens[ind + count][0] > 0:
                            sens[ind+count][0] -= 1
                            exit.append(sens[ind+count][1])
                            count += 1
                        if(len(exit) > 0):
                            output.append("".join(exit))
                        ind += 2

                print outputs.format(case+1, " ".join(output[::-1]))
if __name__ == "__main__":
	main()
