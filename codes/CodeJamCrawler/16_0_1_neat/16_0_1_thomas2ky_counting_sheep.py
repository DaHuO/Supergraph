'''
Created on Apr 8, 2016

@author: Thomas
'''
import numpy as np

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def get_res(s, lim, seen=None, iter_num=1):
    if seen is None:
        seen = []
        
    curr_num = str(iter_num * int(s))
    #print "s: " + str(int(s)) + ", iter_num: " + str(iter_num)  + ", curr_num: " + str(curr_num)
    #print seen
    
    for digit in curr_num:
        if digit not in seen:
            seen.append(digit)
            
    if len(seen) >= 10:
        return [curr_num, iter_num]
    elif iter_num >= lim:
        return ["INSOMNIA", iter_num]
    else:
        return get_res(s, lim, seen, iter_num+1)


if __name__ == '__main__':
    out = {}
    max_iter_num = 0
    with open("A-large.in", 'rb') as f:
        lines = f.readlines()[1:]
            
        for idx,line in enumerate(lines):
            if RepresentsInt(line):
                print(str(int(line)) + "-------------------------------")
                
                lim = np.ceil(float(line) / 10.0) * 100.0
                [out[idx+1], iter_num] = get_res(line, 73)
                if iter_num > max_iter_num:
                    max_iter_num = iter_num

            else:
                print(line)
    print max_iter_num
    with open("output.txt", 'w') as f:
        f.write("")
        for key, val in out.iteritems():
            line = "Case #" + str(key) + ": " + val + "\n"
            f.write(line)