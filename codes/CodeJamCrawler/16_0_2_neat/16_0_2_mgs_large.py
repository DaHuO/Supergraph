fid = open('input.txt')
T = fid.readline().strip()
fout = open('output.txt','w')

#This returns the number of steps to a string of +
#Idea: We could just work from the top, flipping the leading consecutive 
# region to match the next section.  At the end, just flip to +.
#This only depends on the number of mismatches and the sign of the last entry
#It is optimal, because it changes one mismatch every flip, no strategy can do
#more, and we have to remove all mismatches to win.  Cannot flip last sign and
#fix a mismatch in the same move, so there is no better approach.
#Solution: number of mismatches + (1 if last sign is -)
def steps(s):
    #Add 1 if the last sign is negative
    last_sign = 1 if s[-1]=='-' else 0
    
    #Figure out how many sign changes there are
    num_changes = s.count('+-') + s.count('-+')

    #Add these two things
    return last_sign + num_changes

for i,line in enumerate(fid):
    line = line.strip()
    if len(line)==0:
        continue
    out = steps(line)
    fout.write('Case #%d: %s\n' % (i+1, out))
