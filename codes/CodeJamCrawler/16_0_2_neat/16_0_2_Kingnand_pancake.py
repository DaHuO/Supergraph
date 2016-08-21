'''
Created on Apr 9, 2016

@author: kingnand
'''
def flip_cake(line, state):
    if not line:
        return 0
    if '+' not in line and state == 1:
        return 1
    elif '+' not in line and state == 0:
        return 0
    elif '-' not in line and state == 1:
        return 0
    elif '-' not in line and state == 0:
        return 1
    else:
        last_cake = line[-1]
        if '-' == last_cake and state == 1:
            return 1 + flip_cake(line[:-1], 0)
        elif '-' == last_cake and state == 0:
            return flip_cake(line[:-1], 0)
        elif '+' == last_cake and state == 1:
            return flip_cake(line[:-1], 1)
        elif '+' == last_cake and state == 0:
            return 1 + flip_cake(line[:-1], 1)



if __name__ == '__main__':
    with open('out.txt', 'w') as out:
        with open('B-large.in', 'r') as f:
            num=0
            i=0
            for line in f:
                if i==0:
                    num=int(line)
                else:
                    numstep = flip_cake(line.strip(), 1)
                    out.write('Case #' + str(i) + ': ' + str(numstep))
                    if(i != num):
                        out.write('\n')
                i+=1
