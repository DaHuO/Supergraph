def PRS(N, P, R, S):
    if any([x > 1 for x in [P-S, R-P, S-R]]): return "IMPOSSIBLE"
    if N == 1:
        if S == 0: return 'PR'
        if R == 0: return 'PS'
        if P == 0: return 'RS'
    if S%2 == 0: el = [PRS(N-1, P/2, R/2+1, S/2), PRS(N-1, P/2+1, R/2, S/2)]
    if P%2 == 0: el = [PRS(N-1, P/2, R/2+1, S/2), PRS(N-1, P/2, R/2, S/2+1)]
    if R%2 == 0: el = [PRS(N-1, P/2, R/2, S/2+1), PRS(N-1, P/2+1, R/2, S/2)]
    return ''.join(sorted(el))

def main():
    cases = int(raw_input())
    for case in range(1, cases+1):
        N, R, P, S = map(int, raw_input().split())
        print "Case #%i:" %case, PRS(N, P, R, S)
        
if __name__ == '__main__':
   main()
