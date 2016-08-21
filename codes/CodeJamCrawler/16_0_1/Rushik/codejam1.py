
import csv
'''
f = open('C:\Users\Sony\Downloads\A-small-attempt3.in')
i = 0
Number = 0
answer = []
for Input in f:
        if i == 0:
                i = i + 1
        else:
                Number = Number + 1
                Input = Input.replace("\n","")


'''


def calculation(Input):
        InputStr = str(Input)
        Digit = []

        for ds in InputStr:
                if ds in Digit:
                        m = 0
                else:
                        Digit.append(ds)
        Loop = 0
        M = 2
        while Loop == 0:
                NewInput = M * (Input)
                M = M + 1
                NewInputStr = str(NewInput)

                for newds in NewInputStr:
                        if newds in Digit:
                                K = 0
                        else:
                                Digit.append(newds)

                if len(Digit) == 10:
                        Loop = 1
                        Ans = NewInput
                elif M >1000:
                        Loop = 1
                        Ans = 'INSOMNIA'

        return Ans

if __name__ == "__main__":
        import fileinput
        f = fileinput.input()
        T = int(f.readline())

        for case in range(1,T+1):
                for x in f.readline().split():
                        Input = int(x)
                        answer = calculation(Input)
                        print("Case #{0}: {1}".format(case, answer))





'''
answer.append("Case #{}: {}".format(Number,Ans))


with open('A:\\problemA.out', 'wb') as f:
        writerPAu = csv.writer(f, delimiter='\n')
        writerPAu.writerows(answer)

'''

