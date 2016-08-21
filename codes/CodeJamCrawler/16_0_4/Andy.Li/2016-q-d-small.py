# 2016 Africa Qualification Round - D. Fractiles
# https://code.google.com/codejam/contest/6254486/dashboard#s=p3

def pad_num(s, width):
    diff = width - len(s)
    if diff <= 0:
        return s
    else:
        return '0'*diff + s

def guess_original(k):
    # 1 stand for L
    # 0 stand for G
    result = [[1] * k]
    
    i = 1
    while i < 2**k:
        inner = '{0:b}'.format(i)
        padded = pad_num(inner, k)
        comp = map(lambda x : 1 if x=='0' else 0, padded)
        
        result.append(comp)
        i*=2

    return result


def list_add(a, b):
    return [x + y for x, y in zip(a, b)]

def compress(guesses, k, c, i_seg):
    #   000
    #   101
    #   110
    # + 111
    # = 322
    result = []
    if c == 1:
        return reduce(list_add, guesses)
    
    for i_guess in range(len(guesses)):
        if guesses[i_guess][i_seg]:
            #print i_guess, i_seg, guesses[i_guess][i_seg], guesses[i_guess]
            result.append(guesses[i_guess])
            
    return reduce(list_add, result)
    
    
def solve(k, c, s):
    #print 'k, c, s:', k, c, s
    result = []
    
    guesses = guess_original(k)
    #print 'guesses:', guesses

    i_seg = 0
    while len(guesses) > 1 and i_seg < s:
        segment = compress(guesses, k, c, i_seg)        
        min_l = min(segment)
        min_i = segment.index(min_l)
        
        #print 'segment', i_seg, segment , 'min_l:', min_l, 'min_i:', min_i
        guesses = [guess for guess in guesses if guess[i_seg] and guess[min_i]]
        #print 'new guesses:', guesses
        #print

        if c > 1:
            result.append(i_seg*k + min_i + 1)
        else:
            result.append(min_i + 1)
            
        i_seg += 1    

    
    
    if len(guesses) > 1:
        return 'IMPOSSIBLE'
    else:
        return ' '.join(map(str, result))


#input, solve and output:
file = 'D-small-attempt0'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    (k, c, s) = map(int, input.readline().split())
    result = solve(k, c, s)

    result_output = 'Case #%s: %s\n' %(case, result)
    print result_output
    output.write(result_output)

input.close()
output.close()
