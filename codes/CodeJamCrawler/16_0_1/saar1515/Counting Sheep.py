
def readFile(path=r"C:\Users\Saar\Desktop\ap.txt"):
    with open(path,'r') as f:
        lst=f.read().splitlines()
    return lst

def N_to_sleep(number):
    digits_counter=[0,0,0,0,0,0,0,0,0,0]
    counter=0
    repetition_counter=10
    string_number=str(number)
    while counter<10:
        last_counter=counter
        for digit in string_number:
            if digits_counter[int(digit)]==0:
                counter+=1
            digits_counter[int(digit)]=-1
            if(counter==10):
                break
        else:
            if(last_counter==counter):
                repetition_counter+=1
            else:
                repetition_counter=0
            if(repetition_counter>=100):
                print("INSOMNIA")
                return
            string_number=str(int(string_number)+number)
    print(string_number)

if __name__ == '__main__':
    file=readFile(r"C:\Users\Saar\Desktop\A-large.in")
    for number in range(1,len(file)):
        print("Case #"+str(number)+":",end=" ")
        N_to_sleep(int(file[number]))