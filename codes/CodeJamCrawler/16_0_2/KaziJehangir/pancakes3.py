# def flip(node, toFlip):
# 	strIn = list(node[0])
# 	c = node[1]
# 	for i in range(0, toFlip+1):
# 		if strIn[i] == '-':
# 			strIn[i] = '+'
# 		else:
# 			strIn[i] = '-'
# 	# print ("".join(strIn),c+1)
# 	return ("".join(strIn),c+1);

# def findMinFlips(cakeStr, count):
# 	# find how many characters of the string are + from the end
# 	numHappy = 0
# 	for i in range(0, len(cakeStr)):
# 		if cakeStr[len(cakeStr) - i - 1] == '+': # cakeStr[len(cakeStr) - i - 1]
# 			numHappy += 1
# 		else:
# 			break
# 	if numHappy == len(cakeStr):
# 		return count
# 	else:
# 		successors = generateSuccessors(''.join(list(cakeStr)[:end - numHappy]))
# 		return min[findMinFlips(s,count + 1) for s in successors]

# def generateSuccessors(strIn):
# 	output = []
# 	for i in range(1,len(strIn)+1):
# 		output.append(flip(strIn, i))
# 	return output
import Queue

def flip(node, toFlip):
    strIn = list(node[1])
    c = node[2]
    numHappy = node[0]
    for i in range(0, toFlip+1):
        if strIn[i] == '-':
            strIn[i] = '+'
        else:
            strIn[i] = '-'
    # print ("".join(strIn),c+1)
    # find how many characters of the string are + from the end
    count = 0
    for i in range(0, len(strIn)):
        if strIn[len(strIn) - i - 1] == '+':
            count += 1
        else:
            break

    return (len(strIn)-count,"".join(strIn),c+1);
def applyBfs(cakestr):
    toTraverse = Queue.PriorityQueue()
    toTraverse.put((len(cakestr),cakestr, 0))
    while toTraverse.empty() == 0:
        node = toTraverse.get()
        # toTraverse.remove(node)
        # print toTraverse
        # if all([p == '+' for p in node[0]]):
        # print node
        if node[1] == ('+' * len(node[1])): 
            return node;
        
        for i in range(0, len(node[1])):
            toTraverse.put(flip(node, i))
            # print toTraverse
    return -1

numTests = int(raw_input())
for i in range(1, numTests + 1):
    cakestr = raw_input()
    # nodes = [(cakestr, 0)]
    finalstate = applyBfs(cakestr)
    print "Case #{}: {}".format(i, finalstate[2])
