{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Source code file for Google Code Jam user jdemeyer\n",
    "# solving problem A of Qualification Round 2016.\n",
    "#\n",
    "# This is a Jupyter Notebook file to be run with SageMath version 7.2.beta3,\n",
    "# although the precise version probably does not matter that much.\n",
    "#\n",
    "# To open, install SageMath, then run the Jupyter Notebook server with\n",
    "#   sage -n jupyter\n",
    "# and open this file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import os, sys\n",
    "\n",
    "class CodejamProblem(object):\n",
    "    def __init__(self, input):\n",
    "        self.inputlines = iter(input.splitlines())\n",
    "        self.cases = []\n",
    "        \n",
    "    def readint(self):\n",
    "        return ZZ(next(self.inputlines))\n",
    "\n",
    "    def readints(self):\n",
    "        return map(ZZ, next(self.inputlines).split())\n",
    "    \n",
    "    def readline(self):\n",
    "        return next(self.inputlines)\n",
    "        \n",
    "    def solve(self, f=sys.stdout, raw=False):\n",
    "        for i, case in enumerate(self.cases, 1):\n",
    "            ans = self.solvecase(case)\n",
    "            if raw:\n",
    "                ans = repr(ans)\n",
    "            else:\n",
    "                ans = self.formatanswer(ans)\n",
    "            f.write(\"Case #{0}: {1}\\n\".format(i, ans))\n",
    "        f.flush()\n",
    "        \n",
    "    def solvecheck(self, output):\n",
    "        from StringIO import StringIO\n",
    "        out = StringIO()\n",
    "        self.solve(out)\n",
    "        assert out.getvalue() == output\n",
    "            \n",
    "    def formatanswer(self, ans):\n",
    "        return str(ans)\n",
    "    \n",
    "    @classmethod\n",
    "    def autosolve(cls, filename, *args, **kwds):\n",
    "        import datetime, time\n",
    "        out = open(\"/tmp/out\", \"wt\")\n",
    "\n",
    "        print(\"autosolving...\")\n",
    "\n",
    "        nexc = 0\n",
    "        while nexc < 10:\n",
    "            t0 = datetime.datetime.now()\n",
    "            try:\n",
    "                input = open(filename).read()\n",
    "            except IOError:\n",
    "                time.sleep(0.2)\n",
    "                continue\n",
    "            d = datetime.datetime.now() - t0\n",
    "            print(\"Read input in %.2fs\" % d.total_seconds())\n",
    "            \n",
    "            t0 = datetime.datetime.now()\n",
    "            try:\n",
    "                problem = cls(input, *args, **kwds)\n",
    "            except Exception:\n",
    "                from traceback import print_exc\n",
    "                print_exc()\n",
    "                nexc += 1\n",
    "                time.sleep(0.5)\n",
    "                continue\n",
    "            d = datetime.datetime.now() - t0\n",
    "            ncases = len(problem.cases)\n",
    "            print(\"Parsed input in %.2fs, got %s cases\" % (d.total_seconds(), ncases))\n",
    "            \n",
    "            t0 = datetime.datetime.now()\n",
    "            problem.solve(out)\n",
    "            d = datetime.datetime.now() - t0\n",
    "            print(\"Solved problem in %.2fs\" % d.total_seconds())\n",
    "\n",
    "            problem.notify()\n",
    "            return\n",
    "        \n",
    "    @staticmethod\n",
    "    def notify():\n",
    "        os.system(\"mplayer /usr/share/apps/kgoldrunner/themes/default/victory.ogg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "class Problem(CodejamProblem):\n",
    "    def __init__(self, input):\n",
    "        CodejamProblem.__init__(self, input)\n",
    "        \n",
    "        T = self.readint()\n",
    "        for i in range(T):\n",
    "            self.cases.append(self.readint())\n",
    "            \n",
    "    def solvecase(self, case):\n",
    "        if not case:\n",
    "            return \"INSOMNIA\"\n",
    "        chars = set()\n",
    "        N = 0\n",
    "        while len(chars) < 10:\n",
    "            N += case\n",
    "            for x in str(N):\n",
    "                chars.add(x)\n",
    "        return N"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "input=\"\"\"\n",
    "5\n",
    "0\n",
    "1\n",
    "2\n",
    "11\n",
    "1692\n",
    "\"\"\"\n",
    "\n",
    "output=\"\"\"\n",
    "Case #1: INSOMNIA\n",
    "Case #2: 10\n",
    "Case #3: 90\n",
    "Case #4: 110\n",
    "Case #5: 5076\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "input = \"\".join(line+\"\\n\" for line in input.splitlines() if line)\n",
    "output = \"\".join(line+\"\\n\" for line in output.splitlines() if line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 'INSOMNIA'\n",
      "Case #2: 10\n",
      "Case #3: 90\n",
      "Case #4: 110\n",
      "Case #5: 5076\n"
     ]
    }
   ],
   "source": [
    "P = Problem(input)\n",
    "P.solve(raw=True)\n",
    "P.solvecheck(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "autosolving...\n",
      "Read input in 0.00s\n",
      "Parsed input in 0.00s, got 100 cases\n",
      "Solved problem in 0.01s\n"
     ]
    }
   ],
   "source": [
    "P.autosolve(\"/home/jdemeyer/Desktop/A-small-attempt0.in\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "autosolving...\n"
     ]
    }
   ],
   "source": [
    "P.autosolve(\"/home/jdemeyer/Desktop/A-large.in\")"
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
   "display_name": "SageMath 7.2.beta3",
   "language": "",
   "name": "sagemath"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
