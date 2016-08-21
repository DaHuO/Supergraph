import os
import itertools

class Solver(object):
    def __init__(self):
        pass
    
    def solve(self, inputs):
        ss = inputs[0].strip()
        c = [0]*10 
        c[0] = ss.count('Z')
        c[2] = ss.count('W')
        c[4] = ss.count('U')
        c[6] = ss.count('X')
        c[8] = ss.count('G')
        c[7] = ss.count('S') - c[6]
        c[5] = ss.count('F') - c[4]
        c[3] = ss.count('H') - c[8]
        c[9] = ss.count('I') - c[5] - c[6] - c[8]
        c[1] = ss.count('N') - c[9] - c[9] - c[7]
        r = []
        for i, cc in enumerate(c):
            for t in range(cc):
                r.append(str(i))
        return ''.join(r)
        pass
    
    def feed(self, inputs):
        lines = [x.strip() for x in inputs]
        outputs = []
        test_case_n = int(lines[0])
        cur = 1
        for i in range(test_case_n):
            i = i
            case_line_cnt = 1
            case_inputs = lines[cur:cur+case_line_cnt]
            cur += case_line_cnt
            outputs.append(self.solve(case_inputs))
        return outputs

if __name__ == '__main__':
    iname = 'A-large.in'
    sample_in = '''4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER
    '''
    sample_out = '''
Case #1: 012
Case #2: 2468
Case #3: 114
Case #4: 3
    '''
    if os.path.exists(iname):
        with open(iname) as f:
            inputs = f.readlines()
    else:
        inputs = [x.strip() for x in sample_in.split('\n') if x.strip()]
    solver = Solver()
    outputs = solver.feed(inputs)
    fail_flag = False
    if os.path.exists(iname):
        with open(iname+'.out', 'w') as f:
            for i, v in enumerate(outputs):
                print >> f, 'Case #%d: %s'%(i+1, str(v))
    else:
        ans = set([x.strip() for x in sample_out.split('\n') if x.strip()])
        for i, v in enumerate(outputs):
            t = 'Case #%d: %s'%(i+1, str(v))
            if t not in ans:
                print '!!! Wrong:', t
                fail_flag = True
    print '===================================================='
    for i, v in enumerate(outputs):
        print 'Case #%d: %s'%(i+1, str(v))
    print '===================================================='
    print 'done' if not fail_flag else 'fail'
    pass