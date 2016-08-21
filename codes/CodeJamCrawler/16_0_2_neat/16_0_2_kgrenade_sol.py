import sys



def get_steps(str):
    num_steps = 0
    at_front = 1
    on_chunk = 0;
    for i in range(0,len(str)):
        c = str[i]
        
        if i == 0 and c == '-':
            num_steps+=1
            on_chunk = 1
        elif c == '-' and on_chunk == 0:
            num_steps +=2
            on_chunk = 1
        elif c == '+':
            on_chunk = 0
        


        
    return num_steps

def main(in_file):
    with open(in_file, 'r') as f:
        lines = f.readlines()


    num_cases = lines[0]
    cnt = 1
    for line in lines[1:]:
        print("Case #%d: %d" %(cnt, get_steps(line.strip())))
        cnt+=1
        
    

if __name__=="__main__":
    main(sys.argv[1])
