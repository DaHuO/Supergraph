import sys
def main(filePath):
    File = open(filePath,'r').readlines();
    cnt = File.pop(0)
    output = []
    for f in range(int(cnt)):
        output.append(CS(int(File[f]),f))
    out = open('./output.txt','w')
    for o in range(len(output)):
        out.write(output[o]);
    out.close()

def CS(f,i):
    l=[]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    c=1
    Break = False
    Bool = True
    while Bool:
        if int(f)==0:
            return 'Case #'+str(i+1)+': '+str('INSOMNIA')+"\n";
        sheeps0 = f*c
        sheeps = str(sheeps0)
        for sheep in sheeps:
            if sheep not in l:
                l.append(sheep)
                NothingNew = False
        if len(l)==10:
            return 'Case #'+str(i+1)+': '+str(sheeps0)+"\n";
        c+=1



if __name__ == '__main__':
    try:
        filePath = sys.argv[1]
    except(IndexError):
        filePath = raw_input('Enter Path for the file ')
    finally:
        main(filePath)
