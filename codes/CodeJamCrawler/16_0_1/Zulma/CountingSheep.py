def set_numbers(N, seenNumbers):
    for i in str(N):
        seenNumbers[int(i)] = 1
        
        
def check_numbers(seenNumbers):
    return sum(seenNumbers) == 10
    
    
def main():
    T = int(raw_input())  # read a line with a single integer

    for t in range(T):
        N = int(raw_input())
        if N == 0:
            print "Case #{}: {}".format(t+1, "INSOMNIA")
        else:
            all_found = False
            seenNumbers = [0] * 10
            i = 1 
            
            while not all_found:
                Nnew = N * i
                set_numbers(Nnew, seenNumbers)
                all_found = check_numbers(seenNumbers)
                i = i + 1
                
            print "Case #{}: {}".format(t+1, Nnew)

        
if __name__ == "__main__":
    main()
