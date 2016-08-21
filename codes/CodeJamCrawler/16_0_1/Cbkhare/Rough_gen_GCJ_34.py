from sys import stdin as Si
if __name__=='__main__':
    n = int(Si.readline())
    for i in range(n):
        N = int(Si.readline())
        Sol,num = '',1
        if N==0:  Sol = 'INSOMNIA'
        else:
            Num,S,Sol= (),set(),True
            while len(S)!=10:
                _Num = str(N*num)
                if _Num in Num:
                    Sol = False;break
                S.update(set(_Num).difference(S))
                if len(S)==10:  break
                num+=1
            if Sol: Sol = str(N*num)
            else:   Sol = 'INSOMNIA' 
        print('Case #%d: %s'% (i+1, Sol))
                    
                

    
