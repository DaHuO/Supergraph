def main():
    t = int(raw_input())  # read a line with a single integer
    for caseIdx in xrange(1, t + 1):
        # read an integer
        N = int(raw_input())

        remainingNumList = []
        for i in xrange(2*N-1):
            paper = [int(s) for s in raw_input().split(" ")]
            for num in paper:
                if num in remainingNumList:
                    remainingNumList.remove(num)
                else:
                    remainingNumList.append(num)

        remainingNumList.sort()

        print "Case #{}: {}".format(caseIdx, ' '.join(str(num) for num in remainingNumList))

if __name__ == '__main__':
    main()
