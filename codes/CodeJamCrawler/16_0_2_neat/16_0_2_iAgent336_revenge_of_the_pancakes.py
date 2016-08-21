def solve(single_case):
    breakpoint_counter = 0
    last_is_happy = True
    for c in reversed(single_case):
        if(c=='+'): this_is_happy = True
        elif(c=='-'):  this_is_happy = False
        else: print 'ERROR', this_is_happy
        if(this_is_happy^last_is_happy): 
            #print 'bk'
            breakpoint_counter += 1
        #print this_is_happy
        last_is_happy = this_is_happy
    return breakpoint_counter

def main():
    testcases = input()
    for case_num in xrange(1, testcases+1):
        single_case = raw_input()
        print("Case #%i: %s" % (case_num, solve(single_case)))

def test():
    single_case = raw_input()
    print("Case #1: %s" % (solve(single_case)))


if __name__=='__main__':
    main()
    #test()


