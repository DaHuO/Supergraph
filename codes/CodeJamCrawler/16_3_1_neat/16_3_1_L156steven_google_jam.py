
WRITE_FILE = "/Users/stevenliu/Downloads/output.out"

def run_jam(f):
    answers = []
    with open(f) as file:
        inputs = int(file.readline())
        for i in range(0, inputs):
            file.readline()
            answers.append(process_input(file.readline()))

    i = 1
    with open(WRITE_FILE, 'w') as r:
        for answer in answers:
            r.write("Case #{}: {}\n".format(i, answer))
            i += 1

class SenatorCount():

    def __init__(self, char, num):
        self.char = char
        self.num = num

def process_input(line):
    senators = line.split(' ')

    char = 'A'
    # list of characters to numbers

    from Queue import PriorityQueue
    pq = PriorityQueue()

    total = 0
    for senator in senators:
        #senator_tuples.append(SenatorCount(char, senator))
        total += int(senator)
        pq.put((-int(senator), SenatorCount(char, int(senator))))
        char = chr(ord(char) + 1)

    # find highest senator count, subtract 1
    # find the highest senator count againt, subtract 1 (is that ever a problem)
    resp = []

    while not pq.empty():
        p, element1 = pq.get(True)
        total -= 1
        r = element1.char
        if element1.num > 1:
            priority = element1.num - 1
            pq.put((- priority, SenatorCount(element1.char, element1.num - 1)))

        if not pq.empty():
            p, element2 = pq.get(True)

            # check if there's only 1 left and we'd remove this guy
            if pq.qsize() == 1 and element2.num == 1:
                # this is not okay, return it back to the queue
                pq.put((-element2.num, SenatorCount(element2.char, element2.num)))
            else:
                r += element2.char
                if element2.num > 1:
                    priority = element2.num - 1
                    pq.put((-priority, SenatorCount(element2.char, element2.num - 1)))

        resp.append(r)

    return ' '.join(resp)

print process_input('1 1 1')

run_jam("/Users/stevenliu/Downloads/a.in")
