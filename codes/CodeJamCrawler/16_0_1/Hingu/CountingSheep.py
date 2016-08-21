def main():
    for t in xrange(int(raw_input().strip())):
        #print 'Case #'+str(t+1)+':'
        N = int(raw_input().strip())
        if N == 0:
            print 'Case #'+str(t+1)+':', 'INSOMNIA'
            continue
        s = set(); i = 1
        while True:
            y = i*N
            #print N, y, s
            for digit in list(str(y)):
                s.add(digit)
            if len(s) == 10:
                print 'Case #'+str(t+1)+':', y
                break
            i += 1
            
if __name__ == '__main__': 
    main()
