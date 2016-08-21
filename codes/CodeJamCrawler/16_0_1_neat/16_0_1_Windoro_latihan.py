import sys

def freopen(f,option,stream):
  import os
  oldf = open(f,option)
  oldfd = oldf.fileno()
  newfd = stream.fileno()
  os.close(newfd)
  os.dup2(oldfd, newfd)

freopen("input.txt","r",sys.stdin),freopen("output.txt","w",sys.stdout)

def isi(n, angka):
    while n!=0:
        angka [ n%10 ] += 1
        n//=10


t = int( input() )
kasus = 1

while t>0 :
    t-=1
    n = int( input() )
    
    angka = [0,0,0,0,0,0,0,0,0,0]
    kali = 2
    
    if n == 0 : 
        print ("Case #"+ str(kasus) +": INSOMNIA")
        kasus += 1
        continue
    else :
        temp = n
        while True:
            isi(temp, angka)
            
            not_nol_all = True
            for i in angka:
                if i == 0:
                    not_nol_all = False
                    break
                    
            if not_nol_all :
                ans = temp
                break
                
            temp = kali * n
            kali += 1
    
    print ("Case #"+ str(kasus) +": " + str(ans) )
    kasus += 1
    