import sys

def invert_sign(stack):
    new_list = ""
    for i in xrange(len(stack)):
        if stack[i] == "-":
            new_list += "+"
        else:
            new_list += "-"
    return new_list



def invert(lista, original):
    queue = []
    distance = {}
    queue.append(lista)
    distance[lista] = 0
    while len(queue) > 0:
        current = queue.pop(0)
        if current == original:
            return distance[current]
        for i in xrange(1,len(current)+1):
            temp = current[0:i]
            temp = invert_sign(temp)
            temp = temp+current[i:]
            if temp not in distance:
                distance[temp] = distance[current] + 1
                if temp == original:
                    return distance[temp]
                queue.append(temp)
    return False

T = int(sys.stdin.readline().strip())

for i in xrange(T):
    stack = "".join(sys.stdin.readline().strip().split())
    original = ""
    for x in xrange(len(stack)):
        original += "+"


    print "Case #"+str(i+1)+": "+str((invert(stack, original)))