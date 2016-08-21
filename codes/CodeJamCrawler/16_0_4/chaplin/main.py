def problem_2016D_small():
    t=int(raw_input())
    for case in range(1,t+1):
        K,C,S=[int(item) for item in (raw_input().split())]
        print 'Case #'+str(case)+':',
        for i in range(K):
            print i+1,
        print ''
        
def problem_2016D_large():
    pass        
        
        
           
        
def main():

    problem_2016D_small()
    
if __name__ == '__main__':
    main()
