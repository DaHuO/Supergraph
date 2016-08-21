__author__ = 'TOBE'


def solve(astring):
    mainstring = astring[0]
    for i in range(1,len(astring)):
        if astring[i] >= mainstring[0]:
            mainstring = astring[i] + mainstring
        else:
            mainstring = mainstring + astring[i]

    return mainstring


print solve('zxcasdqwe')



solve_codejam = 1

if solve_codejam :


    try:
        input_file = open('A-large.in','r')
        print "opened"
    except IOError:
        input_file = open('test_smal.in','r')
    else:
        pass

    output_file = open('submit.in','w')

    Test_cases = int(input_file.readline())

    for i in range(Test_cases):
        print >>output_file, "Case #%d: %s"%(i +1,solve(input_file.readline().strip()))





    output_file.close()
    print "done"