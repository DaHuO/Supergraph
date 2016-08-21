def lastword(S):
    final = S[0]
    for x in S[1:]:
        final = max(final+x, x+final)
    return final

def main():
    cases = int(raw_input())
    for case in range(1, cases+1):
        print "Case #%i:" %case, lastword(raw_input())

if __name__ == '__main__':
   main()
