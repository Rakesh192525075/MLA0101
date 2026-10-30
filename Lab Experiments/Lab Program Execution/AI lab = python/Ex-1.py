from collections import deque
g = {'A':['B','C'], 'B':['D','E'],
     'C':['F'], 'D':[], 'E':[], 'F':[]}
q = deque(['A'])
visited = []
while q:
    n = q.popleft()
    if n not in visited:
        print(n, end=" ")
        visited.append(n)
        q.extend(g[n])
