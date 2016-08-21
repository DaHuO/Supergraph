import Queue

#Global
ALPHABET = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',
            11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',
            20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}




def senate(num, listSenators):
    q = Queue.PriorityQueue()
    order = list()



    # Put into PQ
    for i in range(num):
        q.put((-(listSenators[i]), ALPHABET[i+1]))


    while not q.empty():
        num, letter = q.get()
        order.append(letter)
        num += 1
        if num < 0:
            q.put((num, letter))

    # print order
    newOrder = list()

    if len(order) % 2 == 0:
        for i in range(0,len(order)-1,2):
            newOrder.append(order[i]+order[i+1])
    else:
        for i in range(0,len(order)-3,2):
            newOrder.append(order[i]+order[i+1])
        newOrder.append(order[-3])
        newOrder.append(order[-2]+order[-1])
    


    return ' '.join(newOrder)


    #newOrder = list()
    # put together
    #for i in range(len(order)):
    #    newOrder


def main():

    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        numberSenators = int(raw_input())
        listSen = [int(s) for s in raw_input().split(" ")]
        #print listSen
        order = senate(numberSenators, listSen)
        # word = aLastWord(raw_input())
        print ("Case #{}: {}".format(i, order))

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#   print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options





if __name__=='__main__':
    main()