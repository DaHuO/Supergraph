def pancakes():
    t =  int(raw_input())
    for i in xrange(1,t+1):
        stack = raw_input()
        moves = 0
        stack = list(stack)
       # print stack
        while(stack[len(stack)-1]!="-"):  #shave off the tail thats good
            stack.pop(len(stack)-1)
            if len(stack)==0:
                break
        #print stack
        c = 0
        while(stack.count("+")!=len(stack)):
            sgn = stack[0]
            index = 0
            while(sgn==stack[index]):
                index+=1
                if(index==len(stack)):
                   break
           # print stack
            top = stack[:index]
            del stack[:index]
            top.reverse()
            top2 = []
            for h in top:
                #print h
                if h== '+':
                    top2.append('-')
                else:
                    top2.append('+')
           # print top2
            #top = ["+" for h in top else "-"]
            stack = top2 + stack
            moves+=1
            if(c==7):
                break

        print "Case #{}: {}".format(i, moves)

pancakes()
