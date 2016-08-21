#f = open("C:\\Downloads\\qwer.txt","r")
#wiki
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
        rrrr = 0
        for edge in self.get_edges(source):
            if self.flow[edge] != 0 :
                rrrr+=1
        return  rrrr
        #return sum(self.flow[edge] for edge in self.get_edges(source))

f = open("C:\\Downloads\\C-small-attempt3.in","r")
lines = f.readlines()
i = 1
pos = 1
while pos < len(lines):
    cur = lines[pos]
    res = 0
    frst = {}
    scnd = {}
    edges = []
    g = FlowNetwork()
    for j in range(1,int(lines[pos])+1):
        pos +=1
        w1,w2 = lines[pos].split()
        edges.append([w1,w2])
        #print  w2
        if w1 in frst:
            frst[w1].add(w2)
        else:
            frst[w1] = set([w2])
        if w2 in scnd:
            scnd[w2].add(w1)
        else:
            scnd[w2] = set([w1])
    g.add_vertex("QQQQQQQQQQQQQQQQQ_1")
    g.add_vertex("QQQQQQQQQQQQQQQQQ_2")
    for q in frst:
        g.add_vertex(q + "________1")
    for q in scnd:
        g.add_vertex(q + "________2")
    for q in frst:
        g.add_edge("QQQQQQQQQQQQQQQQQ_1",q + "________1",1)
    for q in scnd:
        g.add_edge(q + "________2","QQQQQQQQQQQQQQQQQ_2",1)
    for e in edges:
        w1,w2 = e
        g.add_edge(w1+ "________1",w2+ "________2",1)
    qq = len(frst) + len(scnd) - g.max_flow("QQQQQQQQQQQQQQQQQ_1","QQQQQQQQQQQQQQQQQ_2")
    res = len(edges) - qq
    #print g.max_flow("QQQQQQQQQQQQQQQQQ_1","QQQQQQQQQQQQQQQQQ_2")
    pos +=1
    print "Case #" + str(i) +  ": " + str(res)
    i += 1