import sys
import logutil
import yaml
import os
import import_utils

LOG = logutil.initlog('importer')


def recur_loop(line,starting_pos,ending_pos,old_val,new_val,no_of_times):

    
    while line.count(line[0]) <> len(line): 
          ###print "before line", line, no_of_times,ending_pos
          line=line[starting_pos:ending_pos].replace(old_val, new_val) + line[ending_pos:]
          ###if  line.count(line[0]) <> len(line) :
          no_of_times = no_of_times + 1
          #else:
          #  if line[0] == "-" :
          #     print "lines", line
          #     no_of_times = no_of_times + 1
          print "before line", line, no_of_times,ending_pos
          old_val_prev = old_val
          new_val_prev = new_val
          old_val  = new_val_prev
          new_val   = old_val_prev
          ending_pos = line.find(new_val)

    #if line[0] == "+" : 
    #   if line.count(line[0]) == len(line):
    #       return no_of_times 

    if line[0] == "-" :   
       if line.count(line[0]) == len(line):
           no_of_times = no_of_times + 1
 
    return no_of_times  

def check_len(line):

    no_of_times = 0 
    if line[0] == "+" : 
       if line.count(line[0]) == len(line):
          return 0
       else:
          end_position = line.find("-")
          start_position = 0
          old_val = "+"
          new_val = "-"
          return recur_loop(line,start_position,end_position,old_val,new_val,no_of_times)
    
    if line[0] == "-" :
       if line.count(line[0]) == len(line):
          return 1
       else:
          end_position = line.find("+")
          start_position = line.find("-")
          old_val = "-"
          new_val = "+"
          return recur_loop(line,start_position,end_position,old_val,new_val,no_of_times)
          
          

def main(args=None):
    
    target = open("/home/siyer/result.txt", 'w')
    target.truncate()
    f = open("/home/siyer/input.txt")
    next(f)
    cnt= 0
    for line in f:
        cnt = cnt + 1
        linestr = line
        counter= check_len(str.strip(linestr))
        target.write( "Case #"+ str(cnt) + ": "+ str(counter)) 
        target.write("\n")
   
    target.close()

if __name__ == "__main__":
    sys.exit(main())

