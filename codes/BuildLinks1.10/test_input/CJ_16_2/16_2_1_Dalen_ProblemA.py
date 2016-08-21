
INPUT_FILE = 'A-large.in';
OUTPUT_FILE = 'A-small-practice.out';

solvers = [
   [
      { 'let' : 'Z', 'n': 0, 'string': 'ZERO' },
      { 'let' : 'W', 'n': 2, 'string': 'TWO' },
      { 'let' : 'U', 'n': 4, 'string': 'FOUR' },
      { 'let' : 'X', 'n': 6, 'string': 'SIX' },
      { 'let' : 'G', 'n': 8, 'string': 'EIGHT' }
   ],
   [
      { 'let' : 'H', 'n': 3, 'string': 'THREE' },
      { 'let' : 'S', 'n': 7, 'string': 'SEVEN' }
   ],
   [
      { 'let' : 'O', 'n': 1, 'string': 'ONE' },
      { 'let' : 'V', 'n': 5, 'string': 'FIVE' },
      { 'let' : 'I', 'n': 9, 'string': 'NINE' }
   ]
]

def algorithmA(S):
   news = S
   number = []
   for solver in solvers:
      for letter_solver in solver:
         while news.find(letter_solver['let']) >= 0:
            for c in letter_solver['string']:
               news = news.replace(c,'',1)
            number.append(letter_solver['n'])
   number.sort()
   return ''.join(str(x) for x in number)

def solve(data):
   S = data[0]
   return str(algorithmA(S));

def run():
   with open(INPUT_FILE) as in_file:
      lines = in_file.readlines()

   n_tests = int(lines[0]);

   out_file = open(OUTPUT_FILE,'w')

   count = 1
   for i in range(1,len(lines)):
      result = solve([lines[i]])
      string_result = "Case #%d: %s\n" % (count,result)
      out_file.write(string_result);
      print string_result
      count += 1

run()