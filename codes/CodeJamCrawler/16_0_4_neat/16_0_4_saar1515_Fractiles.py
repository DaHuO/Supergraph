


def readFile(path=r"C:\Users\Saar\Desktop\ap.txt"):
    with open(path,'r') as f:
        lst=f.read().splitlines()
    return lst

if __name__ == '__main__':
    file=readFile(r"C:\Users\Saar\Desktop\D-small-attempt0.in")
    del file[0]
    for index,case in enumerate(file):
        print("Case #"+str(index+1)+": ",end="")
        splitted=case.split(" ")
        for i in range(1,int(splitted[0])):
            print(str(i),end=" ")
        print(splitted[0])