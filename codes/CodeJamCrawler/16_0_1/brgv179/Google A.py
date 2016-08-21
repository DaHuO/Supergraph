test_cases = int(raw_input())
def FallSleeporAsleep(N,test):
    if(N=='0'):
        print "Case #"+str(test+1)+": "+"INSOMNIA"
    else:
        i=1;
        given_numberset=set(N)
        count = 1
        while(given_numberset.__len__() <= 9):
            given_numberset=given_numberset|set(str(int(N)*count))
            if(given_numberset.__len__()==10):
                print "Case #"+str(test+1)+": "+str(int(N)*count)
                exit
            count=count+1

for test in range(test_cases):
    N = (raw_input())
    FallSleeporAsleep(N,test)
