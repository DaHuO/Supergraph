
def cal(number):
    "let's start"
    f_list=['N','N','N','N','N','N','N','N','N','N']
    oldstr=number
    count=0
    while (count < 100000):
        count=count+1
        arr=list(oldstr)
        for num in arr:
            f_list[int(num)]='Y'
        string= ''.join(f_list)
        if string.find('N')==-1:
            return  oldstr        
        else :
            oldstr=str(int(number)*count)
    return 'INSOMNIA'


file = open("a")
T = file.readline()
all_the_text=[]

for num in range(1,int(T)+1):
    final=cal(str(int(file.readline())))
    temstr='Case #'+str(num)+': '+final+'\n'
    all_the_text.append(temstr)
    
file_object = open('thefile.txt', 'w+')
file_object.writelines(all_the_text)
file_object.close( )
