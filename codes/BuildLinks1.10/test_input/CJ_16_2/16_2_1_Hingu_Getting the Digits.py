def main():
    for t in xrange(int(raw_input().strip())):
        number = []
        s = sorted(list(raw_input().strip()))
        if 'Z' in s:
            for i in range(s.count('Z')):
                number.append(0)
                s.remove('Z');s.remove('E');s.remove('R');s.remove('O');
        if 'X' in s: 
            for i in range(s.count('X')):
                number.append(6)
                s.remove('S');s.remove('I');s.remove('X');
        if 'G' in s:
            for i in range(s.count('G')):
                number.append(8)
                s.remove('E');s.remove('I');s.remove('G');s.remove('H');s.remove('T');
        if 'U' in s:
            for i in range(s.count('U')):
                number.append(4)
                s.remove('F');s.remove('O');s.remove('U');s.remove('R');
        if 'W' in s:
            for i in range(s.count('W')):
                number.append(2)
                s.remove('T');s.remove('W');s.remove('O');
                
        if 'O' in s and 'N' in s and 'E' in s:
            for i in range(min([s.count('O'), s.count('N'), s.count('E')])):
                number.append(1)
                s.remove('O');s.remove('N');s.remove('E');
        if 'T' in s and 'H' in s and 'R' in s and 'E' in s and s.count('E') >= 2 :
            for i in range(min([s.count('T'), s.count('H'), s.count('R'), s.count('E')])):
                number.append(3)
                s.remove('T');s.remove('H');s.remove('R');s.remove('E');s.remove('E');
        if 'F' in s and 'I' in s and 'V' in s and 'E' in s:
            for i in range(min([s.count('F'), s.count('I'), s.count('V'), s.count('E')])):
                number.append(5)
                s.remove('F');s.remove('I');s.remove('V');s.remove('E');
        if 'S' in s and 'E' in s and 'V' in s and s.count('E') >= 2 and 'N' in s:
            for i in range(min([s.count('S'), s.count('E'), s.count('V'), s.count('N')])):
                number.append(7)
                s.remove('S');s.remove('V');s.remove('N');s.remove('E');s.remove('E');
        if 'N' in s and 'I' in s and s.count('N') >= 2 and 'E'in s:
            for i in range(min([s.count('N'), s.count('I'), s.count('N'), s.count('E')])):
                number.append(9)
                s.remove('N');s.remove('I');s.remove('N');s.remove('E');
        print 'Case #'+str(t+1)+':', ''.join(map(str, sorted(number)))

if __name__ == '__main__': 
    main()
