# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import numpy as np
import copy

t = int(raw_input())
for case in xrange(1, t+1):
    number_parties = int(raw_input())  # read a line with a single integer
    nbs = [int(p) for p in raw_input().split(" ")]
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer = ''
    while ( np.sum(nbs) > 1):
        correct_removal = False
        for i in xrange(0, len(nbs)):
            for j in xrange(0, len(nbs)):
                temp_nbs = copy.deepcopy(nbs)
                temp_nbs[i] -= 1;
                temp_nbs[j] -= 1;
                if (min(temp_nbs) < 0):
                    correct_removal = False;
                elif (np.sum(temp_nbs)/2 < max(temp_nbs)):
                    correct_removal = False;
                else:
                    correct_removal = True;
                    break;
            if correct_removal:
                answer += ' '
                answer += letters[i]
                answer += letters[j]
                nbs[i] -= 1
                nbs[j] -= 1
                break;
        if not (correct_removal):
            for i in xrange(0, len(nbs)):
                temp_nbs = copy.deepcopy(nbs)
                temp_nbs[i] -= 1;
                if (min(temp_nbs) < 0):
                    correct_removal = False;
                elif (np.sum(temp_nbs)/2 < max(temp_nbs)):
                    correct_removal = False;
                else:
                    correct_removal = True;
                    break;
            if correct_removal:
                answer += ' '
                answer += letters[i]
                nbs[i] -= 1
    if (np.sum(nbs) == 1):
        for i in xrange (0,len(nbs)):
            if (nbs[i] == 1):
                answer += ' '
                answer += letters[i]
                # digits = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
                # answer = ''
                # for i in xrange(0,10):
                #     curr_number = True
                #     while curr_number:
                #         curr_number, new = check_nb(number, i)
                #         if curr_number != False:
                #             number = curr_number
                #             answer += new
                # answer = ''.join(sorted(answer))
    print "Case #{}:{}".format(case, answer)
