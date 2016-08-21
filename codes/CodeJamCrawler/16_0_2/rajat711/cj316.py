def remove_adjacent(nums):
    return [a for a,b in zip(nums, nums[1:]+[not nums[-1]]) if a != b]

def countneg(s):
    return s.count('-')

def countfrontneg(s):
    p=s.find('+')
    s=s[0:p]
    return s.count('-')
    
i_file = open("B-large.in","r")
inputs = [line.rstrip('\n') for line in i_file]
i_file.close()
o_file = open("o2.out","w")
cases=1
del inputs[0]
for pcake in inputs:
    pcake=pcake+"+"
    lpcake=list(pcake)
    lpcake=remove_adjacent(lpcake)
    npcake=''.join(lpcake)
    totalneg = countneg(npcake)
    frontneg = countfrontneg(npcake)
    flips = (totalneg - frontneg) * 2
    if frontneg > 0:
        flips += 1
    o_file.write("Case #"+str(cases)+": "+str(flips)+"\n")
    cases +=1
    #print flips
o_file.close()
    
    
    