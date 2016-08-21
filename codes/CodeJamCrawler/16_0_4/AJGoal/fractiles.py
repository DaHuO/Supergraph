# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:35:00 2016

@author: Admin
"""



def fractiles(tcNo,k,c,s,fileOut):
    numbersList = list()
    if c==1 and k!=1:
        for i in range(1,s+1):
            numbersList.append(str(i))
        fileOut.write('Case #{}: {}\n'.format(tcNo,' '.join(numbersList)))
        return
    if k==1:
        fileOut.write('Case #{}: {}\n'.format(tcNo,1))
        return
    if k==2:
        if c==1:
            fileOut.write('Case #{}: {}\n'.format(tcNo,' '.join(['1','2'])))
        else:
            fileOut.write('Case #{}: {}\n'.format(tcNo,2))
        return
    if s==1 and k>1:
        fileOut.write('Case #{}: {}\n'.format(tcNo,'IMPOSSIBLE'))
        return 
    for i in range(1,k+1):
        numbersList.append(str(i))
    
    fileOut.write('Case #{}: {}\n'.format(tcNo,' '.join(numbersList)))

def main():
    fileOut = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\FractilesSmall.txt','w')
    fileIn = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\D-small-attempt1.in','r')
    
    noOfTcs = int(fileIn.readline())
    for tc in range(1,noOfTcs+1):
        k,c,s = fileIn.readline().strip('\n').split()
        fractiles(tc,int(k),int(c),int(s),fileOut)
    
    
    fileOut.flush()
    fileOut.close()
    fileIn.close()
main()