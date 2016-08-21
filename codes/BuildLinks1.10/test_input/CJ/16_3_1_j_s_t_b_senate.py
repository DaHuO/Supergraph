
filename = "A-large"
#filename = "A-minimal"
with open(filename + ".in", 'r') as inputfile:
    lines = inputfile.readlines()

number_of_tests = int(lines[0].strip())
print(number_of_tests, "tests")

def sort_senates(s):
    assert type(s) == list
    return sorted(s, key = lambda x: x[1], reverse=True)
    
def has_majority(s_in):
    s = sort_senates(s_in)
    maxvotes = s[0][1]
    other_votes = 0
    for i in range(1,len(s)):
        other_votes += s[i][1]
    #print("MAX", maxvotes, "OTHER", other_votes)
    return (maxvotes > other_votes)


def has_remaining(s_in):
    return bool(total_sen(s_in))
    
def total_sen(s_in):
    total = 0
    for sen in s_in:
        total += sen[1]
    #print("TOTAL", total)
    return total

def evacuate(s_in):
    s = sort_senates(s_in)
    
    if remaining_parties(s) == 1:
        raise ValueError("Only one party")
    
    if remaining_parties(s) == 2:
        if s[0][1] > s[1][1]:
            s[0][1] -= 1
            return s, s[0][0]
        else:
            s[0][1] -= 1
            s[1][1] -= 1
            return s, s[0][0]+s[1][0]
    
    # 3 or more parties    
    if s[0][1] - s[1][1] >= 2:
        s[0][1] -= 2
        return s, s[0][0]*2
   
    if remaining_parties(s) >= 4:
        if s[0][1] > 1:
            s[0][1] -= 2
            return s, s[0][0]*2
        else:
            s[0][1] -= 1
            s[1][1] -= 1
            return s, s[0][0]+s[1][0]
    
    else: # 3 remaining parties
        if s[0][1] == 1:
            s[0][1] -= 1
            return s, s[0][0]
        else:
            s[0][1] -= 1
            s[1][1] -= 1
            return s, s[0][0]+s[1][0]
            
def remaining_parties(s_in):
    parties = 0
    for sen in s_in:
        if sen[1]:
            parties += 1
    return parties


with open(filename + ".out", 'w') as outputfile:

    for testnumber in range(1, number_of_tests+1):
        row_start = -1 + testnumber*2
        row_stop = testnumber*2
        line_start = lines[row_start]
        line_stop = lines[row_stop]
        
        # Read number of senators per party
        splitted_start = line_start.strip().split()
        assert len(splitted_start) == 1
        number_of_parties = int(splitted_start[0])
        
        partynames = []
        for i in range(ord('A'), ord('A')+number_of_parties):
            partynames.append(chr(i))
        assert len(partynames) == number_of_parties
        #print(partynames)
        
        splitted_stop = line_stop.strip().split()
        assert len(splitted_stop) == number_of_parties
        counts = []
        for token in splitted_stop:
            counts.append(int(token))
        
        senators =  [list(t) for t in zip(partynames, counts)]
        
        # Evacutate            
        evacuationlist = []
        while has_remaining(senators):
            print(senators)
            #print("REM1", remaining_parties(senators))
            senators, evac = evacuate(senators)
            #print(senators)
            #print("REM2", remaining_parties(senators))
            #print("EV", evac)
            assert 0 < len(evac) <=2
            evacuationlist.append(evac)
            assert not has_majority(senators)

        result = " ".join(evacuationlist)
        
        answer = "Case #{}: {}\n".format(testnumber, result)
        print(answer)
        outputfile.write(answer)

