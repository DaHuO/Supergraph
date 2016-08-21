__author__ = 'TOBE'


def IncludeN(main_dict,counter,N):

    for item in str(N):
        if not main_dict[item]:
            main_dict[item] = 1
            counter[0] += 1


#
# def NoteAllFound(main_dict,N):
#     for i in range(0,10):
#         if main_dict[str(i)] >= 1:
#             pass
#         else:
#             main_dict[str(i)] = 1

def PreCompute(N):
    if str(N) == '0':
        return 'INSOMNIA'
    main_dict = {'0':0,'1':0, '2':0,'3':0,\
                 '4':0,'5':0,'6':0,'7':0,\
                 '8':0,'9':0}

    counter = [0]

    k = 0

    while 1:
        k += 1
        New_N = N*k

        IncludeN(main_dict,counter,New_N)

        if counter[0] >= 10:
            break
    return k



try:
    input_file = open('A-large.in','r')
except IOError:
    print "could not_open google file"
    input_file = open('test_large.in','r')
else:
    pass

output_file = open('submit_large.in','w')

Test_cases = int(input_file.readline())

for i in range(Test_cases):

    N = int(input_file.readline())
    if N != 0:
        print >>output_file, "Case #%d: %d"%(i+1,N*PreCompute(N))
    else:
        print >>output_file, "Case #%d: INSOMNIA"%(i + 1)



