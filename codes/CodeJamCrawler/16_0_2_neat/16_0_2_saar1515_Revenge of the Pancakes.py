


def readFile(path=r"C:\Users\Saar\Desktop\ap.txt"):
    with open(path,'r') as f:
        lst=f.read().splitlines()
    return lst

def pancake_solver(minuses,starting_minus=True):
    if(starting_minus):
        return((minuses-1)*2)+1
    return ((minuses-1)*2)+2

def sequence_reader(sequence):
    allow=True
    minus_counter=0
    for char in sequence:
        if(allow and char=='-'):
            minus_counter+=1
            allow=False
        elif(char=='+'):
            allow=True
    starting_minus=(sequence[0]=='-')
    return (minus_counter,starting_minus)

if __name__ == '__main__':
    file=readFile(r"C:\Users\Saar\Desktop\B-large.in")
    del(file[0])
    for index,sequence in enumerate(file):
        read_sequence=sequence_reader(sequence)
        solution=pancake_solver(read_sequence[0],read_sequence[1])
        print("Case #"+str(index+1)+": "+str(solution))