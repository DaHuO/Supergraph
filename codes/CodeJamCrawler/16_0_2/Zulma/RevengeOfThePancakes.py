

# def switchMainPart(pile):
        # firstEl = pile[0]
        
        # pile[0] = 1 - pile[0]
        # i = 1
        # while i < len(pile) and pile[i] == firstEl:
            # pile[i] = 1 - pile[i]
            # i = i + 1 

# def main():
    # T = int(raw_input())  # read a line with a single integer

    # for t in range(T):
        # pile = raw_input()
        # pile = pile.replace('-','0')
        # pile = pile.replace('+','1')
        # pile = list(pile)
        # pile = [int(i) for i in pile]
        # reverse = 0
        
        # correct_order = sum(pile) == len(pile)
        # while not correct_order:
            # switchMainPart(pile)
            # reverse = reverse + 1
            # correct_order = sum(pile) == len(pile)
                
        # print "Case #{}: {}".format(t+1, reverse)


def main():
    T = int(raw_input())  # read a line with a single integer

    for t in range(T):
        pile = raw_input()
        currentEl = pile[0]
        
        i = 1
        changed = 0
        while i < len(pile):
            if pile[i] != currentEl:
                changed = changed + 1
                currentEl = pile[i]
            i = i + 1
            
        if pile[-1] == '-':
            changed = changed + 1
        
                
        print "Case #{}: {}".format(t+1, changed)    

if __name__ == "__main__":
    main()