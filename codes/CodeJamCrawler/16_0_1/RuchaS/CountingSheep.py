import sys

def main():
  with open("A-large.in","r") as f:
    T = int(f.readline())
    ll = []
    for line in f:
      ll.append(int(line.strip()))
  #print T
  #print ll
  
  compare = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  for i in xrange(T):
    N = ll[i]
    digit_list = []
    if N == 0:
      sys.stdout.write("Case #"+str(i+1)+": INSOMNIA")
    else:
      k = 1
      while True:
        M = k * N
        k = k + 1 
        #print N
        for j in xrange(36):
          digit_list.append(M%10)
          M = M/10
          if M == 0:
            break
        #print digit_list
        if set(digit_list) == set(compare):
          sys.stdout.write("Case #"+str(i+1)+": "+str((k-1)*N))
          break
    sys.stdout.write("\n")

if __name__ == '__main__':
  main()
