



def main():
    T = int(raw_input())
    for i in range(1, T+1):
        K, C, S = [int(s) for s in raw_input().split(" ")]
        simpleSequence = range(1,K**C+1, K**(C-1))
        simpleSequence = [str(j) for j in simpleSequence]
        simpleSequence = " ".join(simpleSequence)
        #print simpleSequence
        print ("Case #{}: " + simpleSequence).format(i)

if __name__ == "__main__":
    main()