import sys
from Queue import PriorityQueue

def senate_evacuation(argv):
	with open(argv[0], 'r') as f:
		t = int(f.readline())
		for i in range(t):
			n = f.readline().strip()
			p = f.readline().strip().split()
			p = [int(x) for x in p]
			all_senate = sum(p)
			pqueue = PriorityQueue()
			for idx, x in enumerate(p):
				pqueue.put((-x, idx + ord('A')))
			sol = []
			while all_senate > 0:
				top1, top2 = pqueue.get(), pqueue.get()
				if top2[0] != 0:
					if sum([x * 100 > (all_senate-2) * 50 for idx,x in enumerate(p) if (not ((idx == top1[1] - ord('A'))\
						or (idx == top2[1] - ord('A'))))]) == 0:
						sol.append(chr(top1[1]) + chr(top2[1]))
						all_senate -= 2
						p[top1[1] - ord('A')] -= 1
						p[top2[1] - ord('A')] -= 1
						pqueue.put((top1[0]+1, top1[1]))
						pqueue.put((top2[0]+1, top2[1]))
					else:
						sol.append(chr(top1[1]))
						all_senate -= 1
						p[top1[1] - ord('A')] -= 1
						pqueue.put((top1[0]+1, top1[1]))
						pqueue.put((top2[0], top2[1]))
				else:
					sol.append(chr(top1[1]))
					all_senate -= 1
					p[top1[1] - ord('A')] -= 1
					pqueue.put((top1[0]+1, top1[1]))
					pqueue.put((top2[0], top2[1]))
			print "Case #%d:" % (i+1),
			print " ".join(sol)


if __name__ == "__main__":
	senate_evacuation(sys.argv[1:])