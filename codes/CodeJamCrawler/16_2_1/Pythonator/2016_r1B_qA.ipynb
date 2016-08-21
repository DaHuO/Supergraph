{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import io, sys, difflib, itertools\n",
    "class InputReader(object):\n",
    "    def __init__(self, input_stream, debug=False):\n",
    "        self._stream = input_stream\n",
    "        self._lines = (line.rstrip('\\n') for line in input_stream)\n",
    "        if debug: self._lines = tuple(self._lines)\n",
    "        self._lines_iter = iter(self._lines)\n",
    "    def lines(self, n=None):\n",
    "        lines_tup = tuple(itertools.islice(self._lines_iter, n))\n",
    "        assert n is None or len(lines_tup) == n\n",
    "        return lines_tup\n",
    "    def chars(self, n=None):\n",
    "        chars = tuple(self.line())\n",
    "        assert n is None or len(chars) == n\n",
    "        return chars\n",
    "    def words(self, n=None):\n",
    "        words = tuple(self.line().split())\n",
    "        assert n is None or len(words) == n\n",
    "        return words\n",
    "    def ints(self, n=None): return tuple(map(int, self.words(n)))\n",
    "    def digits(self, n=None): return tuple(map(int, self.chars(n)))\n",
    "    def floats(self, n=None): return tuple(map(float, self.words(n)))\n",
    "    def line(self): return self.lines(1)[0]\n",
    "    def char(self): return self.chars(1)[0]\n",
    "    def word(self): return self.words(1)[0]\n",
    "    def int(self): return self.ints(1)[0]\n",
    "    def digit(self): return self.digits(1)[0]\n",
    "    def float(self): return self.floats(1)[0]\n",
    "def solve_cases(inp, out):\n",
    "    t = inp.int()\n",
    "    for i in range(1, t + 1):\n",
    "        out.write('Case #{}: '.format(i))\n",
    "        solve_case(inp, out)\n",
    "        out.write('\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def chars_to_vector(chars):\n",
    "    v = np.zeros(26)\n",
    "    for c in chars:\n",
    "        v[ord(c) - ord('A')] += 1\n",
    "    return v\n",
    "\n",
    "digit_vectors = np.zeros((26, 10))\n",
    "for i, text in enumerate((\"ZERO\", \"ONE\", \"TWO\", \"THREE\", \"FOUR\", \"FIVE\", \"SIX\", \"SEVEN\", \"EIGHT\", \"NINE\")):\n",
    "    digit_vectors[:, i] = chars_to_vector(text)\n",
    "\n",
    "def solve(inp, out):\n",
    "    solve_cases(inp, out)\n",
    "\n",
    "def solve_case(inp, out):\n",
    "    global v\n",
    "    text = inp.word()\n",
    "    text_v = chars_to_vector(text)\n",
    "    v = np.linalg.lstsq(digit_vectors, text_v)[0].round()\n",
    "    result = ''.join(str(i) * count for i, count in enumerate(v))\n",
    "    out.write(result)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Anaconda3\\lib\\site-packages\\ipykernel\\__main__.py:21: DeprecationWarning: using a non-integer number instead of an integer will result in an error in the future\n"
     ]
    }
   ],
   "source": [
    "TEST_IN = \"\"\"4\n",
    "OZONETOWER\n",
    "WEIGHFOXTOURIST\n",
    "OURNEONFOE\n",
    "ETHER\"\"\"\n",
    "TEST_OUT = \"\"\"Case #1: 012\n",
    "Case #2: 2468\n",
    "Case #3: 114\n",
    "Case #4: 3\n",
    "\"\"\"\n",
    "\n",
    "def test_solver():\n",
    "    if TEST_IN:\n",
    "        test_in = io.StringIO(TEST_IN)\n",
    "        test_out = io.StringIO()\n",
    "        solve(InputReader(test_in), test_out)\n",
    "        test_out_str = test_out.getvalue()\n",
    "        if test_out_str != TEST_OUT:\n",
    "            print(''.join(difflib.ndiff(TEST_OUT.splitlines(True), test_out_str.splitlines(True))))\n",
    "            raise RuntimeError('TEST_IN and TEST_OUT did not match.')\n",
    "            \n",
    "test_solver()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Anaconda3\\lib\\site-packages\\ipykernel\\__main__.py:21: DeprecationWarning: using a non-integer number instead of an integer will result in an error in the future\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    input_stream = sys.stdin and open(r\"C:\\Users\\Joseph\\Downloads\\A-small-attempt0.in\")\n",
    "    out = sys.stdout and open(r\"C:\\Users\\Joseph\\Downloads\\A-small-attempt0.out\", 'w')\n",
    "    inp = InputReader(input_stream)\n",
    "\n",
    "    solve(inp, out)\n",
    "    \n",
    "if __name__ == '__main__': main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
