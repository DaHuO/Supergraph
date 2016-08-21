"""
# FINAL - SINGLE THREAD


f = open("c.in")
o = open("c.out", "w")

def all_perms(elements):
	if len(elements) <=1:
		yield elements
	else:
		for perm in all_perms(elements[1:]):
			for i in range(len(elements)):
				yield perm[:i] + elements[0:1] + perm[i:]

T = int(f.readline().strip())
print T
for t in xrange(T):
	N = int(f.readline().strip())
	fs = [v-1 for v in map(int, f.readline().strip().split(" "))]
	
	maxl = 0
	for i in xrange(2**N-1, -1, -1):
		b = "{0:b}".format(i)
		b = "0"*(N-len(b))+b
		ns = [pos for pos in xrange(len(b)) if b[pos] == "1"]
		
		if len(ns) > maxl:
			print "(Case %d/%d) Testing with: %d" % (t+1, T, len(ns))
			ns_set = set(ns)
			
			valid1 = True
			for n in ns:
				if not fs[n] in ns_set:
					valid1 = False
					break
			
			valid2 = False
			if valid1:
				lst = [ns[0]]
				valid2 = True
				for i in xrange(len(ns)-1):
					if fs[lst[-1]] in lst:
						valid2 = False
						break
				if valid2:
					if fs[lst[-1]] != lst[0]:
						valid2 = False
			if valid2:
				maxl = len(ns)
				break
	
	ln = "Case #%d: %d" % (t+1, maxl)
	print ln
	o.write(ln + "\n")


o.close()
f.close()







exit()

"""
# MULTITHREAD

import Queue
import threading

class myThread(threading.Thread):
	def __init__(self, tid):
		threading.Thread.__init__(self)
		self.tid = tid
		pass
		
	def run(self):
		global T, lock, queue
		while True:
			lock.acquire()
			if queue.empty():
				lock.release()
				break
			t, fs = queue.get()
			lock.release()
		
			N = len(fs)
			maxl = 0
			for i in xrange(2**N-1, -1, -1):
				b = "{0:b}".format(i)
				b = "0"*(N-len(b))+b
				ns = [pos for pos in xrange(len(b)) if b[pos] == "1"]
				
				if len(ns) > maxl:
					print "(Case %d/%d, thread %d) Testing with: %d" % (t+1, T, self.tid, len(ns))
					ns_set = set(ns)
					
					valid1 = True
					for n in ns:
						if not fs[n] in ns_set:
							valid1 = False
							break
					
					valid2 = False
					if valid1:
						f0 = fs[ns[0]]
						ns = [ns[0]] + [f0] + ns[1:ns.index(f0)] + ns[ns.index(f0)+1:]
						tail = ns[2:]
						for perm_x in all_perms(ns[2:]):
							perm = ns[:2] + perm_x
							valid2 = True
							for j in xrange(len(perm)):
								if not fs[perm[j]] in [perm[j-1], perm[(j+1)%len(perm)]]:
									valid2 = False
									break
							if valid2:
								break
					
					if valid2:
						maxl = len(ns)
						#break
			lock.acquire()
			CASES[t] = maxl
			lock.release()

CASES = {}

def all_perms(elements):
	if len(elements) <=1:
		yield elements
	else:
		for perm in all_perms(elements[1:]):
			for i in range(len(elements)):
				yield perm[:i] + elements[0:1] + perm[i:]


f = open("c.in")

T = int(f.readline().strip())
print T

threads = []

lock = threading.Lock()
queue = Queue.Queue(T)

for t in xrange(T):
	N = int(f.readline().strip())
	fs = [v-1 for v in map(int, f.readline().strip().split(" "))]
	queue.put((t, fs))
f.close()

for tid in xrange(2):
	thread = myThread(tid)
	thread.start()
	threads.append(thread)



for t in threads:
	t.join()

o = open("c.out", "w")
for t in xrange(T):
	ln = "Case #%d: %d" % (t+1, CASES[t])
	print ln
	o.write(ln + "\n")
o.close()






exit()

# SINGLE THREAD


f = open("c.in")
o = open("c.out", "w")

def all_perms(elements):
	if len(elements) <=1:
		yield elements
	else:
		for perm in all_perms(elements[1:]):
			for i in range(len(elements)):
				yield perm[:i] + elements[0:1] + perm[i:]

T = int(f.readline().strip())
print T
for t in xrange(T):
	N = int(f.readline().strip())
	fs = [v-1 for v in map(int, f.readline().strip().split(" "))]
	
	maxl = 0
	for i in xrange(2**N-1, -1, -1):
		b = "{0:b}".format(i)
		b = "0"*(N-len(b))+b
		ns = [pos for pos in xrange(len(b)) if b[pos] == "1"]
		
		if len(ns) > maxl:
			print "(Case %d/%d) Testing with: %d" % (t+1, T, len(ns))
			ns_set = set(ns)
			
			valid1 = True
			for n in ns:
				if not fs[n] in ns_set:
					valid1 = False
					break
			
			valid2 = False
			if valid1:
				tail = ns[1:]
				for perm_x in all_perms(tail):
					perm = [ns[0]] + perm_x
					valid2 = True
					for j in xrange(len(perm)):
						if not fs[perm[j]] in [perm[j-1], perm[(j+1)%len(perm)]]:
							valid2 = False
							break
					if valid2:
						break
			
			if valid2:
				maxl = len(ns)
	
	ln = "Case #%d: %d" % (t+1, maxl)
	print ln
	o.write(ln + "\n")


o.close()
f.close()
