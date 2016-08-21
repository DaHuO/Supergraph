def read_word(f):
    return next(f).strip()

def read_int(f, b=10):
    return int(read_word(f), b)

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    return [reader(f, *args, **kwargs) for i in range(R)]

#..............................................................................


def read_case(f):
    num=read_int(f)
    R = read_ints(f)
    return (num,R)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')


#..............................................................................

#global variables
alph=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def begin(fn='a', out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(1,T+1):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i, res)



#..............................................................................

def solver(case):
    sen=case[1]
    result=""
    while(1):
        m = max(sen)
        if(m==0):
            return result[:-1   ]
        bigList=[i for i, j in enumerate(sen) if j == m]
        if(m==1 and len(bigList)==3):
            pos=bigList[0]
            sen[pos]-=1
            result = result + alph[pos] + " "
        elif(len(bigList)==1):
            pos=bigList[0]
            sen[pos]-=1
            result = result + alph[pos] + " "
        elif(len(bigList)>1):
            p1,p2=bigList[0],bigList[1]
            sen[p1]-=1
            sen[p2]-=1
            result = result + alph[p1] + alph[p2] + " "


begin('L')
