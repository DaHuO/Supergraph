#!/usr/bin/env python2.7
import sys

def test(case,line) :

  c = line[0]
 
  if line[-1] == '-' :
    d = 1
  else :
    d = 0

  for x in line [1:] :
    if c != x :
      d += 1
    c = x

  print 'Case #%s: %s' % (case,d) 

def main () :

  if len(sys.argv) != 2 :
    sys.exit ( 'usage: %s <filename>' % sys.argv[0] )

  filename = sys.argv[1]

  with open( filename , "rb" ) as f :
    lines = f.readlines()

  case = 1

  for line in lines[1:]:
    test (case,line.strip())
    case += 1


if __name__ == '__main__':
  main()
