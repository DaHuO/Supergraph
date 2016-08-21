"""
se inizio con -
      cerca il primo +
      se trovo il +
          cambia tutti i - in + fino al + trovato compreso
          mosse++
      se non trovo il +
          sol = mosse + 1


se inizio con +
    cerca il primo -
    se trovo il -
        cambia tutti i + in - fino al - trovato compreso
        mosse++
    se non trovo il meno
        sol = mosse
"""

def solve(test_case):
    s = raw_input()
    moves = 0

    # print "Start: " + s
    while 1:
        if s[0]=='-':
            plus_index = s.find("+")
            if plus_index!=-1:
                # cambia tutti i - in + fino al + trovato compreso
                replacing_str = plus_index * "+"
                s = replacing_str + s[plus_index:]
                # print "Debug: " + s
                moves += 1
            else:
                print "Case #" + str(test_case) + ": " + str(moves+1)
                return
        else:
            minus_index = s.find("-")
            if minus_index!=-1:
                # cambia tutti i + in - fino al - trovato compreso
                replacing_str = minus_index * "-"
                s = replacing_str + s[minus_index:]
                # print "Debug: " + s
                moves += 1
            else:
                print "Case #" + str(test_case) + ": " + str(moves)
                return



def main():
    t = int(raw_input())
    for i in  xrange(t):
        solve(i+1)

if __name__=="__main__":
    main()
