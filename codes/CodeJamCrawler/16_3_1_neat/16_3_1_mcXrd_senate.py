
import filehandler

import operator

import copy

'''

sorted_x = sorted(x.items(), key=operator.itemgetter(1))
'''

def main():
    
    alphabet = "A    B    C    D    E    F    G    H    I    J    K    L    M    N    O    P    Q    R    S    T    U    V    W    X    Y    Z"
    alphabet = alphabet.replace(" ", "")
    #return alphabet
    
    input = filehandler.Read('A-small-attempt0.in')[1:]
    
    cases = []
    
    odd = True
    for one in input:
        if odd is False:
            cases.append(one)    
        if odd:
            odd=False
        else:
            odd=True
    
    
    
    def solveCase(case):
        ret = ''
        a = case.split(' ')
        
        index = 0
        
        hm = {}
        for one in a:
            hm[alphabet[index]]= int(one)
            index +=1
        
        '''
        temphm = copy.deepcopy(hm)
        sorted_hm = sorted(temphm.items(), key=operator.itemgetter(1))
        '''
        #return hm
        revhm = {}
        for one in hm:
            revhm[one]=0
            
        #return revhm
        revret=''
        while True:
            diffhm = {}
            for one in hm:
                diffhm[one]= hm[one]-revhm[one]
                
            sorted_hm = sorted(diffhm.items(), key=operator.itemgetter(1))
            

            
            biggest1 = sorted_hm[-1][1]
            biggestindex1 = sorted_hm[-1][0]
            
            biggest2 = sorted_hm[-2][1]
            biggestindex2 = sorted_hm[-2][0]
            
            
            if biggest1:
                revret +=biggestindex1
                revhm[biggestindex1] +=1
            
            
            
            
            if biggest2:
                revret += biggestindex2
                revhm[biggestindex2] +=1
            revret +=' '
            
            #print revret
                
            if sorted_hm[0][1]==0:
                revret = revret[:-1] 
                break            

                
            
        a = revret.split(' ')
        a.reverse()
        ret =''
        for one in a:
            ret+=one+' '
        return ret
        
    #return solveCase(cases[2])
    
    counter =0
    writeres = []
    for one in cases:
        counter+=1
        a = solveCase(one)
        
        if a[0]==' ':
            a = a[1:]
        if a[-1]==' ':
            a = a[:-1]
        
        r ='Case #'+str(counter)+': '+a.rstrip()
        writeres.append(r)
        
        
    filehandler.Write('Output.txt',writeres)














