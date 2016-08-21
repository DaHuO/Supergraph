import sys

name="./small.txt"

def convertVec(vect):
    return [True if a == '+' else False for a in vect]

def isEnd(vect):
    _value = True
    for value in vect:
        _value = _value and value
    return _value

def flip(vect, i):

    resp = []

    # if i is 0, flip just the first one and leave the rest
    if i == 0:
        resp.append(not vect[0])
        if len(vect)>1:
            resp.extend(vect[1:])
        return resp

    if i == len(vect)-1:
        return [not a for a in vect]

    resp.extend([not a for a in vect[:i+1]])
    resp.extend([a for a in vect[i+1:]])
    return resp
    

def algo1(tt, vect):

    i = 0


    while(True):
        if isEnd(vect):
            return i
        if len(vect) == 1:
            return 1
        # find index
        for j in xrange(len(vect)):
            if not vect[len(vect)-1-j]:
                # flip!
                vect = flip(vect, len(vect)-1-j)
                i = i+1
                continue


def check():
    fl_wrt = open(name + "_reply", 'r')
    fl_real = open(name + "_real", 'r')

    for line_1 in fl_wrt.readline():
        line_2 = fl_real.readline()
        if line_2 != line_1:
            print('Line do not match:\n{0}{1}'.format(line_1, line_2))

    fl_real.close()
    fl_wrt.close()

def main():

    global name

    if len(sys.argv) > 1:
        #if sys.argv[1] == 'check':
        #    check()
        #    return 0
        #else:
        name = sys.argv[1]

    fl = open(name, 'r')
    fl_wrt = open(name + "_reply", 'w')

    tt = int(fl.readline())
    i = 0

    reply = ''

    while (i < tt):
        i = i+1
       
        numb = fl.readline().rstrip()
        vect = convertVec(numb)

        res1 = algo1(tt, vect)

        reply = reply + "Case #{0}: {1}\n".format(i, res1)

    fl_wrt.write(reply)

    fl.close()
    fl_wrt.close()


if __name__ == "__main__":
    main()
