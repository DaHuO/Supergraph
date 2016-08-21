#qpy:2
#qpy:console
#qpy:http://qpython.com/s/qpy-sample.py

f = open("/storage/emulated/0/output1.txt", "w")
f.write  ("Case #1:\n")
for i in range (500):
  num = 2**15+1+2*i
  s = "{0:b}".format(num)
  f.write (s+s)
  for j in range (2,11):
    f.write (" " + str (int (s,j)))
  f.write ("\n")
f.close ()