if __name__ == "__main__":
    while 1:
        try:
            numberOfCase = int(raw_input(''))
            for i in xrange(numberOfCase):
                N = int(raw_input(''))
                after = [0,1,2,3,4,5,6,7,8,9]
                if N == 0:
                    print 'Case #{0}: INSOMNIA'.format(i+1)
                else:
                    z = 1
                    while 1:
                        r = N*z
                        strR = str(r)
                        for j in xrange(11):
                            if str(j) in strR and j in after: 
                                after.remove(j);
                        if not after:
                            print 'Case #{0}: {1}'.format(i+1, str(r))
                            break
                        z = z + 1
        except (EOFError):
            break

