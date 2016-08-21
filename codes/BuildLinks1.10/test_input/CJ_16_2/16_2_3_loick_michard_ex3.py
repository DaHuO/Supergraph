from collections import Counter

n=input()

class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v  
        self.capacity = w
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)

class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
 
    def add_vertex(self, vertex):
        self.adj[vertex] = []
 
    def get_edges(self, v):
        return self.adj[v]
 
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path( edge.sink, sink, path + [edge]) 
                if result != None:
                    return result
 
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))

def compute(words):
  firsts = []
  seconds = []
  for word in words:
    firsts.append(word[0])
  for word in words:
    seconds.append(word[1])
  firsts = Counter(firsts)
  seconds = Counter(seconds)
  total = 0
  #for word in words:
  #  if firsts[word[0]] > 1 and seconds[word[1]] > 1:
  #    total += 1
  #    firsts[word[0]] -= 1
  #    seconds[word[1]] -= 1
  #print 'BEGIN'
  g = FlowNetwork()
  [g.add_vertex('F-'+v) for v in firsts]
  [g.add_vertex('S-'+v) for v in seconds]
  [g.add_vertex(w[0]+' '+w[1]) for w in words]
  g.add_vertex('**')
  g.add_vertex('||')
  for v in firsts:
    g.add_edge('**','F-'+v,firsts[v] - 1)
    #print ('**','F-'+v,firsts[v] - 1)
  for v in seconds:
    g.add_edge('S-'+v,'||',seconds[v] - 1)
    #print ('S-'+v,'||',seconds[v] - 1)
  for w in words:
    g.add_edge('F-'+w[0],w[0]+' '+w[1],1)
    g.add_edge(w[0]+' '+w[1],'S-'+w[1],1)

    #print ('F-'+w[0],w[0]+' '+w[1],1)
    #print (w[0]+' '+w[1],'S-'+w[1],1)
  print (g.max_flow('**','||'))

for x in xrange(n):
  h = input()
  words = []
  for _ in range(h):
    c, j = raw_input().split(' ')
    words.append((c,j))
  print 'Case #'+str(x+1)+':',
  compute(words)