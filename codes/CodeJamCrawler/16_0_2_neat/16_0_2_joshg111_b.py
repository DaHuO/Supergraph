import fileinput


def find_min_flips(s):
    s_i = iter(s)
    last_c = s_i.next()
    res = 0
    for c in s_i:
        if c != last_c:
            # Found group. 
            if c == '-':
                # Found +- group. 
                for c in s_i:
                    if c != '-':
                        break
                res += 2
                last_c = '+'
                
            elif c == '+':
                # Found -+ group. 
                res += 1
                last_c = '+'

        else:
            last_c = c
            
    if last_c == '-':
        # Special case. We never found a grouping. All pankaces are -...
        res += 1
        
    return res
    


if __name__ == "__main__":
    
    f = open('workfile', 'w')
    i = 1
    f_i = fileinput.input()
    tests = f_i.next()
    for line in f_i:
        res = find_min_flips(line)
        f.write("Case #" + str(i) + ": " + str(res) + "\n")
        i += 1
        
    f.close()
    f_i.close()
    
    
    