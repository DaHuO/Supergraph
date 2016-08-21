import sys



def get_sol(num_str):
    val = int(num_str)
    seen_set = set(num_str)
    coef = 2
    currval = -1
    if val == 0:
        return 0
    else:
        while(len(seen_set) < 10):
            currval = val*coef
            coef+=1
            seen_set = seen_set.union(set(str(currval)))
        return currval

def main(in_file):
    with open(in_file, 'r') as f:
        lines = f.readlines()


    num_cases = lines[0]
    cnt = 1
    for line in lines[1:]:
        val= get_sol(line.strip())
        if val > 0:
            print("Case #%d: %d" %(cnt, get_sol(line.strip())))            
        else:
            print("Case #%d: INSOMNIA" %(cnt))
        cnt+=1
        
    

if __name__=="__main__":
    main(sys.argv[1])
