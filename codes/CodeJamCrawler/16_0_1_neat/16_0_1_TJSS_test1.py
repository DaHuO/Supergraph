__author__ = 'tegjyot'
import fileinput

def testComputeIterations(N):
    dict=[0 for i in range(10)]
    last_number=N
    while sum(dict)<10:
        str_num=str(last_number)
        for i in str_num:
            if dict[int(i)]!=1:
                dict[int(i)]=1

        if sum(dict)<10:
            last_number+=N
    return last_number



# Basic setup
if __name__ == "__main__":
    f = fileinput.input()
    T=int(f.readline())
    for case in range(1,T+1):
         N = [int(x) for x in f.readline().split()][0]

         Output='INSOMNIA'
         if N!=0:
             Output=testComputeIterations(N)

         print("Case #{0}: {1}".format(case, Output))