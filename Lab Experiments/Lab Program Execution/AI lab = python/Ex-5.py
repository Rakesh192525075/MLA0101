import heapq
g = {'A':['B','C'], 'B':['D'],
     'C':['D'], 'D':[]}
h = {'A':4, 'B':2, 'C':1, 'D':0}
q = [(h['A'], 'A')]
visited = []
while q:
    _, n = heapq.heappop(q)
    if n not in visited:
        print(n, end=" ")
        visited.append(n)
        for x in g[n]:
            if x not in visited:
                heapq.heappush(q, (h[x],x))
