
def main():
  T = int(raw_input())
  for t in range(T):
    s = raw_input()
    prevC = s[0]
    flips = 0;
    for i in range(len(s)):
      if (i !=0 and s[i] != prevC):
        flips += 1
        prevC = s[i]
    if (prevC == '-'):
      flips+=1
    
    print("Case #{}: {}".format(t+1, flips))

if __name__ == "__main__":
  main()
