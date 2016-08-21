filein = open('C:\\sb\\Prog\\Python\\gcg16\\B-large-practice.txt')
fileout = open('C:\\sb\\Prog\\Python\\gcg16\\B-large-practice-out.txt','w')

line = filein.readline()
noOfIter=int(line)
   
for iterNo in range(noOfIter):
   line=filein.readline()
   str1=line.strip()
   pancakes=list(str1)
   num = len(pancakes)
   output=0
   if num==1:
      if pancakes[0] == '-':
         output=1
      else:
         output=0
   else:
      prev = pancakes[0]
      for pancake in pancakes[1:]:
         if prev != pancake:
            output += 1
         prev=pancake
      
      if pancakes[-1] == '-':
         output += 1
   print 'Case #{}: {}'.format(iterNo+1, output)
   print>> fileout, 'Case #{}: {}'.format(iterNo+1, output)         
