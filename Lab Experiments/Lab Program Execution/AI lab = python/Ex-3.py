import heapq
g = {'A':[('B',1),('C',4)],
     'B':[('D',2)], 'C':[('D',1)], 'D':[]}
q = [(0, 'A')]
visited = []
while q:
    cost, n = heapq.heappop(q)
    if n not in visited:
        print(n, cost)
        visited.append(n)
        for x, w in g[n]:
            heapq.heappush(q, (cost+w, x))
