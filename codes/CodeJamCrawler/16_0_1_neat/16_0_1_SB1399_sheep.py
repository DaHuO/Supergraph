if __name__ == "__main__":
   
   filein = open('C:\\sb\\Prog\\Python\\gcg16\\A-large-practice.txt')
   fileout = open('C:\\sb\\Prog\\Python\\gcg16\\A-large-practice-out.txt','w')

   line = filein.readline()
   noOfIter=int(line)
   for iterNo in range(noOfIter):
      line=filein.readline()
      num=int(line)
      #print line
      #print type(line)
      reqList = ['0','1','2','3','4','5','6','7','8','9']
      success=0
      for factor in range(1,9999):
         newnum = factor*num
         #print newnum
         numList = list(str(newnum))
         for digit in numList:
            #print digit
            if digit in reqList:
               reqList.remove(digit)
         if len(reqList) == 0:
            success=1
            break
      if success==1:
         output = newnum
      else:
         output = "INSOMNIA"
      print 'Case #{}: {}'.format(iterNo+1, output)
      print>> fileout, 'Case #{}: {}'.format(iterNo+1, output)
         
      