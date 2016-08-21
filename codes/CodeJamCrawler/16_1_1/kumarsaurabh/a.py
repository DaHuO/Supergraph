import itertools

def main():
   T = int(raw_input())
   for c in range(1, T+1):
      S = str(raw_input())
      winStr = []
      winStrLen = 0
      for ch in S:
         if winStrLen == 0:
            winStr += [ch]   
         elif ch < winStr[0]:
            winStr += [ch]
         else:
            winStr = [ch] + winStr
         winStrLen = winStrLen + 1
      print "Case #"+str(c)+":",''.join(winStr)

main()
