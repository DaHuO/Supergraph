#!/usr/bin/env python2.7
import sys

def test(case,value):

  if value == 0 :
    print 'Case #%s: INSOMNIA' % case
    return

  seen = set()
  n = 1

  while True :

    v = n * value

    seen.update ( set( list(str(v)) ) )

    if False not in [ str(x) in seen for x in range(0,10)] :
      print 'Case #%s:' % case , v
      return
 
    n += 1

def main () :

  if len(sys.argv) != 2 :
    sys.exit ( 'usage: %s <filename>' % sys.argv[0] )

  filename = sys.argv[1]

  with open( filename , "rb" ) as f :
    lines = f.readlines()

  case = 1

  for line in lines[1:]:
    test (case,long(line))
    case += 1


if __name__ == '__main__':
  main()
