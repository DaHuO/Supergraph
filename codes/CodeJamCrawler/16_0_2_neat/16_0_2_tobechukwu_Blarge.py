__author__ = 'TOBE'



def flip_string(astring,k):
    flip_dict = {'-':'+','+':'-'}
    c = list(astring[:k])
    b = list(astring)
    for i in xrange(k):
        c[i] = flip_dict[c[i]]

    c.reverse()
    b[:k] = c
    flipped_string = "".join(b)

    return flipped_string


# print flip_string('--+-',4)
def SolveFlip(astring):
    bstring = astring
    counter = 0
    N = len(bstring) - 1
    # print "starting with ",bstring
    for i in range(N,-1,-1):
        if bstring[i] == '+':
            # print 'the i = ',i,'th item is +'
            # raw_input('enter')
            pass
        else:
            # print 'the i = ',i,'th item is -'
            # check if the first item is '+'
            if bstring[0] == '-':
                bstring = flip_string(bstring,i+1)
                counter += 1
                # print "flipped the whole array. the new array is",bstring
                # raw_input('enter')
            else:
                # this means that astring[0] = +
                # find the last occurenct of +
                dummystring = list(bstring[:i])
                dummystring.reverse()
                dummystring = "".join(dummystring)
                k = i -  dummystring.find('+') - 1  # this gives the index of the last occurence of '+'

#                print "last occurence of + occurs at ",k
#                raw_input('enter')

                bstring = flip_string(bstring,k+1)
                # print "flipped the first k =  ", k+1,"array items. the resulting array is ",bstring
                # raw_input('enter')
                bstring = flip_string(bstring,i+1)
                # print "then flipped the first i =  ", i+1,"array items. the resulting array is ",bstring
                # raw_input('enter')
                counter += 2
    return counter

######## Test cases
##print SolveFlip('+-+-')
##print SolveFlip('-+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
##print SolveFlip('+++-+')
##
##print SolveFlip('-+')
##print SolveFlip('----')
##print SolveFlip('++--')
##print flip_string('+-++',4)

#######




solve_codejam = 1

if solve_codejam :

    try:
        input_file = open('B-large.in','r')
        print "Opened it"
    except IOError:
        print "could not open it, Open test case instead"
        input_file = open('test_large.in','r')
        output_file = open('test_large_result.in','w')
    else:
        output_file = open('submit_large.in','w')



    Test_cases = int(input_file.readline())

    for case in xrange(Test_cases):
        line = input_file.readline().strip()
##        print "************************************************************************"
##        print "For Case #",case+1
##        print "current line ", line
        result = "Case #%d: %d"%(case +1, SolveFlip(line))
##        print "number of steps = ",result
##        print "************************************************************************"
        print >>output_file,result
##        raw_input('enter')

    output_file.close()

