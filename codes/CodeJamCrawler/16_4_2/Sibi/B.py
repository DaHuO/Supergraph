import sys, itertools, multiprocessing

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

def dostuff(subset):
      subset_prob = 0.0
      for split in itertools.combinations(subset,len(subset)/2):
        diff = list(subset)
        for x in split:
          diff.remove(x)
        diff = [1-x for x in diff]
        split_prob = reduce(lambda x, y: x*y, split)
        split_prob *= reduce(lambda x, y: x*y, diff)
        subset_prob += split_prob
      return subset_prob

p = multiprocessing.Pool(8)

for t in range(T):
    line = iFile.readline().strip().split()
    
    N = int(line[0])
    K = int(line[1])
    
    prob = [float(x) for x in iFile.readline().strip().split()]
    
    max_prob = 0.0
       
    temp = p.map(dostuff,itertools.combinations(prob,K)) 
    
    max_prob = max(temp)
    
    output = str(max_prob)
    
    print("Case #"+str(t+1)+": "+output)
