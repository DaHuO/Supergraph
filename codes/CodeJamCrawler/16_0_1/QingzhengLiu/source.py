def counting_sheep(num):
   base=set(['0','1','2','3','4','5','6','7','8','9'])
   compare=set()
   for i in range(100):
      result=str(int(num)*(i+1))
      for digit in result:
         if digit not in compare:
            compare.add(digit)
            if compare==base:
               return result
   else:
      return 'INSOMNIA'

if __name__ == "__main__":
   fopen=open('test.in')
   output=open('output.txt', 'a')
   line_num=0
   for lines in fopen:
      if(line_num==0):
         line_num=line_num+1
         continue
      num=lines.strip()
      output.write('Case #'+str(line_num)+': ')
      output.write(counting_sheep(num)+'\n')
      line_num = line_num + 1
   output.close()
