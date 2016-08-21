import threading

class SolveThread(threading.Thread):
    
    def __init__(self, threadId):
        threading.Thread.__init__(self)
        self.threadId = threadId

    def run(self):
        while len(work_queue) > 0:
            queue_lock.acquire()
            if len(work_queue) == 0:
                return
            num, count = work_queue.pop()
            if queue_lock.locked():
                queue_lock.release()
            i = 1
            digits = [0]*10
            itermax = 1000
            iter_count = 0

            while iter_count < itermax:
                n_i = i * num
                
                i += 1

                while n_i >= 1:
                    digit = n_i % 10
                    n_i = n_i/10
                    digits[digit] = 1

                    if all(digits):
                        answer_lock.acquire()
                        answers[count] = (i-1)*num
                        answer_lock.release()
                        iter_count = itermax + 1
               

                if iter_count < itermax:
                    iter_count += 1
                else:
                    break

            if count not in answers:
                answer_lock.acquire()
                answers[count] = -1
                print answers
                answer_lock.release()
        
        return 

answer_lock = threading.Lock()
answers = {}

thread_count = 10

queue_lock = threading.Lock()
work_queue = []

filename = 'in.in'
f = open(filename,'r')
lines = f.readlines()
f.close()

total_count = int(lines[0])

for i in xrange(1,total_count+1):
    work_queue.append((int(lines[i].strip()), i))

thread_list = []
for j in xrange(thread_count):
    t = SolveThread(j)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

outfilename = 'out.txt'
out = open(outfilename, 'w')

for i in xrange(1,total_count+1):
    if answers[i] == -1:
        print "Case #%d: INSOMNIA" % i
        out.write("Case #%d: INSOMNIA\n" % i)
    else:
        print "Case #%d: %d" % (i, answers[i])
        out.write("Case #%d: %d\n" % (i, answers[i]))

out.close()

