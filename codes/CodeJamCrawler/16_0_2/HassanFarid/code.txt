def flip(s):
    s_list = list(s)
    for i in xrange(len(s_list)):
        if s_list[i] == '-':
            s_list[i] = '+'
        elif s_list[i] == '+':
            s_list[i] = '-'
    return ''.join(s_list)
def do_flip(tray):
    total_flips = 0
    lower_bouund = tray.rfind('-')
    while lower_bouund >= 0:
        focus = tray[:lower_bouund+1]
        done = tray[lower_bouund+1:]
        neg_upper_bound = focus.find('-')
        pos_upper_bound = focus.find('+')
        #neg on top
        if neg_upper_bound == 0:
            tray = flip(focus) + done
        elif pos_upper_bound >=0 and neg_upper_bound > 0:
            local_done = focus[neg_upper_bound:]
            local_focus = focus[:neg_upper_bound]
            tray = flip(local_focus) + local_done + done
        total_flips = total_flips + 1
        print "After flip " + str(total_flips) + ": " + tray
        lower_bouund = tray.rfind('-')
    return total_flips


# Open input file
file_in = open("B-small-attempt0.in", "r")
file_out = open("output.txt", "w")

T = int(file_in.readline())
print "Total test cases: " + str(T)

for i in xrange(T):
    line = file_in.readline().rstrip('\n')
    print "Test case: " + str(i+1) + " - N: " + line + " Length: " + str(len(line))
    out = str(do_flip(line))
    file_out.write("Case #" + str(i+1) + ": " + out + '\n')
    print out

#Close file
file_in.close()
file_out.close()