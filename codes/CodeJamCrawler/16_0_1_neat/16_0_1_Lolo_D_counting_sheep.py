def distinct_digits(n):
    return set(map(int,str(n)))

def count_to_sleep(n):
    if n == 0:
        return "INSOMNIA"
    
    digit_set = set()
    counter=n
    while len(digit_set) < 10:
        digit_set.update(distinct_digits(counter))
        counter += n
    return counter-n
        
        
def main(filename):
    with open(filename) as fin:
        data = map(int,fin.read().split())
    cases = next(data)
    with open('out.txt','w') as fout:
        for i,n in enumerate(data):
            fout.write("Case #{}: {}\n".format(i+1,count_to_sleep(n)))
        

if __name__ == '__main__':
    main('A-large.in')
