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
'''    Q1 = read_arr(f, 4)
    R2 = read_int(f)
    Q2 = read_arr(f, 4)
'''
    

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')


#..............................................................................

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



def solver(c):
    m=c    
    p=2
    ctr=False
    d=dict()
    dig='0987654321'
    n=m
    for j in dig:
        d[j]=0
    while ctr==False and m!=0:        
        for k in str(n):
            d[k]+=1
        for l in d.values():
            if l==0:
                ctr=False
                break
            else:
                ctr=True
        n=m*p
        p+=1
    if ctr==True:
        return str(m*(p-2))
    elif m==0:
        return "INSOMNIA"


begin('c')
