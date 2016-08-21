import sys


class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.edges = {}

    def addEdge(self, v, w):
        if v not in self.edges:  # init
            self.edges[v] = set()
        self.edges[v].add(w)
        self.E += 1

    def removeEdge(self, v, w):
        if w in self.adj(v): self.edges[v].remove(w)

    def adj(self, v):  # vertices pointing from v
        return self.edges.get(v, [])

    def vs(self):
        return [v for v in self.edges]

    def reverse(self):
        rev = Graph(self.V)
        for v in self.edges:
            for w in self.edges[v]:
                rev.addEdge(w, v)
        return rev

    def __str__(self):
        ans = ''
        for v in self.edges:
            for w in self.adj(v):
                ans += '{}->{}\n'.format(v, w)
        return ans


class DFS:
    def __init__(self, G):
        # self.marked = {}
        self.max_path = []
        self.current_path = []
        self.components = {}
        self.counter = 0
        self.topologicalOrder = []
        self.G = G

        for v in range(G.V):
            if v not in self.components:
                self.dfs(v)
                self.counter += 1

        self.topologicalOrder.reverse();

    def dfs(self, v):
        # print 'visit', v
        # self.marked[v] = True
        self.components[v] = self.counter
        self.current_path.append(v)
        for w in self.G.adj(v):
            if w not in self.components:
                self.dfs(w)
                self.current_path.pop()
            else:
                # print 'cycle', w, current_path
                if len(self.current_path) > len(self.max_path):
                    self.max_path[:] = self.current_path[:]

        self.topologicalOrder.append(v)

    def _height(self, v, visited={}):
        if v is None or v in visited: return 0
        visited[v] = 1
        ns = [self._height(w, visited) + 1 for w in self.G.adj(v) if w not in visited]
        return 0 if len(ns) == 0 else max(ns)

    def heightOf(self, v, visited):
        return self._height(v, visited)


def getHeight(G, w, height, marked):
    marked[w] = True
    adj = G.adj(w)
    if len(adj) == 0: return height
    hs = [getHeight(G, n, height + 1, marked) for n in adj if n not in marked]
    if len(hs) == 0: return height
    return max(hs)


def heightFrom(G, v):
    marked = {}
    return getHeight(G, v, 0, marked)


def solveQuadratic(f):
    bf = map(int, f.readline().split())
    bf.insert(0, None)  # 1 based index

    ans = 0
    chains = [0] * len(bf)
    for i in xrange(1, len(bf)):
        v = i
        visit = [False] * len(bf)
        l = 0
        while not visit[v]:
            visit[v] = True
            l += 1
            v = bf[v]

        if bf[bf[v]] == v:
            chains[v] = max(chains[v], l - 1)  # avoid double counting the other side, w-(v)<-b<-a
        elif v == i:
            ans = max(ans, l)

    # print 'ans', bf, ans, chains
    return max(ans, sum(chains))


with open(sys.argv[1] + '.in', 'r') as f:
    with open(sys.argv[1] + '.out', 'w') as fo:
        T = int(f.readline())

        for t in xrange(1, T + 1):
            N = int(f.readline())
            P = map(int, f.readline().split())

            getParty = lambda x: chr(ord('A') + x) if x > -1 else ''
            res = []
            print 'vals ', P
            while sum(P) > 0:
                dist = [1.*i/sum(P) for i in P if sum(P) > 0]
                if len([i for i in dist if i > 0.5]) > 0:
                    print 'wrong', dist

                ind1 = P.index(max(P))
                if P[ind1] > 0:
                    P[ind1] -= 1
                else:
                    ind1 = None
                ind2 = P.index(max(P))
                if P[ind2] > 0:
                    P[ind2] -= 1
                else:
                    ind2 = None

                print ind1, ind2
                dist = [1.*i/sum(P) for i in P if sum(P) > 0]
                if len([i for i in dist if i > 0.5]) > 0:
                    P[ind2] += 1
                    ind2 = None

                res.append('{}{}'.format(getParty(ind1), getParty(ind2)))

            ans = ' '.join(res)
            ans = "Case #{}: {}\n".format(t, ans)
            print ans,
            fo.write(ans)
