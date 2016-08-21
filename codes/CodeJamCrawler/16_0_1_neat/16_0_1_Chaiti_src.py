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
    R1 = read_int(f)
    return (R1)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')


#..............................................................................

#global variables
lis=[0,1,2,3,4,5,6,7,8,9]


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

def solver(i):
        if(i==0):
            return('INSOMNIA')
        else:
            curr_list=lis[:]
            mult=1
            while(1):
                it=str(i*mult)
                for k in it:
                    curr_list[int(k)]=None
                mult+=1
                for j in curr_list:
                    if j is not None:
                        break
                else:
                    return (it)

begin('c')
